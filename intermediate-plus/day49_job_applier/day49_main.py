from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from api_key_secret import *

def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Set up Selenium driver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3830762619&f_AL="
           "true&f_SB2=6&f_WT=2&keywords=business%20analyst&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

# Start sign in
sleep(2)
sign_in = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in.click()

# Log in
sleep(2)
username = driver.find_element(by=By.ID, value='username')
username.send_keys(LI_USERNAME)
password = driver.find_element(by=By.ID, value='password')
password.send_keys(LI_PASSWORD)
sign_in = driver.find_element(by=By.CSS_SELECTOR, value=".btn__primary--large")
sign_in.click()

# Find the first job and apply
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3830762619&f_AL="
           "true&f_SB2=6&f_WT=2&keywords=business%20analyst&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

# Get Listings
sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

sleep(5)
driver.quit()

pass
