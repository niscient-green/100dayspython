# Stock trading terminal
from twilio.rest import Client
import requests

# Set globals, constants -----------------------------------------------------------------------------------------------
# Endpoints
ALPHA_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"

# Stock to follow
STOCK_SYM = "MSFT"
STOCK_NAME = "Microsoft"

# Other
DELTA_TRIGGER = 0.05
delta: float


# Get stock price ------------------------------------------------------------------------------------------------------
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stock_price() -> bool:
    global delta

    # Make stock price request
    alpha_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_SYM,
        "apikey": ALPHAVANTAGE_KEY,
    }
    alpha_request = requests.get(url=ALPHA_ENDPOINT, params=alpha_params)
    alpha_request.raise_for_status()
    alpha_data = alpha_request.json()["Time Series (Daily)"]

    # Sort through data to get 2 most recent days
    alpha_data_lst = [value for (key, value) in alpha_data.items()]
    most_recent_close = float(alpha_data_lst[0]["4. close"])
    second_most_recent_close = float(alpha_data_lst[1]["4. close"])

    # Determine if the delta is sufficient to trigger headlines
    delta = (most_recent_close - second_most_recent_close) / second_most_recent_close
    if abs(delta) >= DELTA_TRIGGER:
        return True
    else:
        return False


# Get news headlines ---------------------------------------------------------------------------------------------------
def get_news() -> list:
    # Get news headlines
    news_params = {
        "apiKey": NEWSAPI_KEY,
        "q": "Microsoft",
        "pageSize": "3",
    }
    news_request = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_request.raise_for_status()
    news_data = news_request.json()

    # Sort out top 3 news headlines
    news_top_headlines = []
    for article in news_data["articles"]:
        news_top_headlines.append(article["title"])
    return news_top_headlines


# Send SMS with headlines ----------------------------------------------------------------------------------------------
def send_sms(news_top_headlines: list):
    # Determine if delta if positive
    global delta
    if delta > 0:
        delta_symbol = "🔺"
    else:
        delta_symbol = "🔻"

    # Send SMS for each headline
    client = Client(TWILIO_ID, TWILIO_KEY)
    for headline in news_top_headlines:
        message = client.messages.create(
          from_="+18888279180",
          body=f"{STOCK_SYM}: {delta_symbol}{int(abs(delta*100))}%\nHeadline: {headline}\n",
          to="+13037473448",
        )

        print(message.sid)


# Main program loop ----------------------------------------------------------------------------------------------------
if get_stock_price():
    news_top_headlines = get_news()
    send_sms(news_top_headlines=news_top_headlines)
