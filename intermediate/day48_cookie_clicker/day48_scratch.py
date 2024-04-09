from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Set up Selenium driver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Fanttik-Screwdriver-Precision-E1-MAX/dp/B0BGWRWRX2?th=1")

# Class name
whole_price = float(driver.find_element(By.CLASS_NAME, "a-price-whole").text)
fraction_price = float(driver.find_element(By.CLASS_NAME, "a-price-fraction").text)
price = whole_price + (fraction_price / 100)

# Name
search_bar = driver.find_element(By.NAME, "field-keywords")
placeholder = search_bar.get_attribute("placeholder")

# ID
button = driver.find_element(By.ID, "nav-search-submit-button")
size = button.size

# CSS Selector
title = driver.find_element(By.CSS_SELECTOR, value=".a-size-large product-title-word-break")

# XPath
script = driver.find_element(By.XPATH, '//*[@id="nav-belt"]/div[2]/script[2]')
script_link = script.text


# Close a tab
# driver.close()

# Close Chrome
driver.quit()

pass