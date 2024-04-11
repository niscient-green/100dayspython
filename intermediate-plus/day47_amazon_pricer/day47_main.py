from bs4 import BeautifulSoup
import requests
import lxml
from api_keys_secret import *
import smtplib

# Scrape Amazon product page, send notification when reaches target price

# Set globals
TARGET_PRICE = 200.00

# Scrape Amazon product page
amazon_url = "https://www.amazon.com/Fanttik-Screwdriver-Precision-E1-MAX/dp/B0BGWRWRX2?th=1"
amazon_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
amazon_response = requests.get(url=amazon_url, headers=amazon_headers)
amazon_markup = amazon_response.content
amazon_soup = BeautifulSoup(markup=amazon_markup, features='lxml')

# Find the price of the product
price_tag = amazon_soup.find(id="attach-base-product-price")
price = float(price_tag.get('value'))


# Function to send an email
def send_email():
    # Create email notification body
    message_body = f"Low price alert. {amazon_url}"
    recipient_email = RECIPIENT_EMAIL
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=recipient_email,
                msg="Subject: Amazon price alert"
                    f"\n\n{message_body}"
            )
    except smtplib.SMTPRecipientsRefused:
        print("Error: recipient address not valid")


# Send email if price is less than target price
if price < TARGET_PRICE:
    send_email()
