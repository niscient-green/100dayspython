from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Set up Selenium driver
driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.wikipedia.org/")
#
# article_count_ele = driver.find_element(By.CSS_SELECTOR, value='#js-link-box-en small')
# article_count = article_count_ele.text.split('+')[0]
# print(article_count)

# article_count_ele.click()

# wiki_func = driver.find_element(By.LINK_TEXT, value='Wikifunctions')
# wiki_func.click()

# search_box = driver.find_element(By.NAME, value='search')
# search_box.send_keys('Python', Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, value='fName')
fname.send_keys('Testing')
lname = driver.find_element(By.NAME, value='lName')
lname.send_keys('Lasty')
email = driver.find_element(By.NAME, value='email')
email.send_keys('tlasty@whoever.com')

signup = driver.find_element(By.CSS_SELECTOR, value='form button')
signup.click()

# Close Chrome
# driver.quit()

pass
