from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Set up Selenium driver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Element tracking -----------------------------------------------------------------------------------------------------
# Main cookie to click
cookie = driver.find_element(By.ID, value='cookie')

# Stats
cps = driver.find_element(By.ID, value='cps')
upgrade_elements = None
upgrade_names = []
upgrade_costs = []


# Helper functions -----------------------------------------------------------------------------------------------------
def get_upgrades():
    # Bring in globals, reset them
    global upgrade_elements, upgrade_names, upgrade_costs
    upgrade_names = []
    upgrade_costs = []
    upgrade_elements = driver.find_elements(By.CSS_SELECTOR, value='[id^=buy]')

    # Parse out the name and cost into lists
    for n in range(0, len(upgrade_elements) - 1):
        name = upgrade_elements[n].text.split(' -')[0]
        cost = int(upgrade_elements[n].text.split('\n')[0].split('- ')[1].replace(',', ''))
        upgrade_names.append(name)
        upgrade_costs.append(cost)

    # Reverse both lists so the highest cost item is first
    upgrade_names = upgrade_names.reverse()
    upgrade_costs = upgrade_costs.reverse()


def get_money():
    # Get total current money
    money = driver.find_element(By.ID, value='money')
    return int(money.text)


def buy_upgrades():
    # Buy upgrades, most expensive cost first
    while True:
        get_upgrades()
        money_int = get_money()
        for cost in upgrade_costs:
            if money_int >= cost:
                


# Main program ---------------------------------------------------------------------------------------------------------
n = 0
while n < 20:
    cookie.click()
    n += 1

# buy_upgrades()
get_upgrades()

# Close Chrome
# driver.quit()

pass
