from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Set up Selenium driver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Element tracking -----------------------------------------------------------------------------------------------------
# Main cookie to click
cookie = driver.find_element(By.ID, value='cookie')

# Get upgrade item ids.
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

# Set timer
timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

# Stats
cps = driver.find_element(By.ID, value='cps')
cookie_upgrades = {}
upgrade_costs = []


# Helper functions -----------------------------------------------------------------------------------------------------
def get_upgrades():
    global cookie_upgrades, upgrade_costs

    # Get all upgrade <b> tags
    all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
    item_prices = []

    # Convert <b> text into an integer price.
    for price in all_prices:
        try:
            element_text = price.text
        except:
            print("Stale")
        else:
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

    # Create dictionary of store items and prices
    cookie_upgrades = {}
    for n in range(len(item_prices)):
        cookie_upgrades[item_prices[n]] = item_ids[n]

    # Create list of costs for easy sorting
    upgrade_costs = [cost for cost in cookie_upgrades.items()]
    upgrade_costs.sort(reverse=True)

    return


def get_money():
    # Get total current money
    money = int(driver.find_element(By.ID, value='money').text.replace(',',''))
    return money


def buy_upgrades():
    get_upgrades()
    money = get_money()

    # Buy upgrades, most expensive cost first
    while money >= upgrade_costs[-1][0]:
        buy_most_expensive(money)
        get_upgrades()
        money = get_money()


def buy_most_expensive(money: int):
    for upgrade in upgrade_costs:
        if money >= upgrade[0]:
            to_purchase_id = upgrade[1]
            driver.find_element(by=By.ID, value=to_purchase_id).click()
            return


# Main program ---------------------------------------------------------------------------------------------------------
while True:
    cookie.click()

    if time.time() > timeout:
        buy_upgrades()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break


# Close Chrome
# driver.quit()

pass
