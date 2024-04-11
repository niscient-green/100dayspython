from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Set up Selenium driver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# Find events By XPath
# links = {}
# for n in range(1, 6):
#     event_date_raw = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li'
#                                                          f'[{str(n)}]/time').get_attribute('datetime')
#     event_date = event_date_raw.split('T')[0]
#     event = driver.find_element(By.XPATH,
#                                 value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{str(n)}]/a').text
#     links[n - 1] = {'date': event_date, 'name': event}


# Find events by class selector
event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
events = {}
for n in range(0, len(event_times)):
    events[n] = {
        'time': event_times[n].text,
        'name': event_names[0].text,
    }

# Close Chrome
driver.quit()

pass
