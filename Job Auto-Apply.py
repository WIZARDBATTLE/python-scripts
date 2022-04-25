import os
import time
import logging
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

logging.basicConfig(level=logging.INFO)

load_dotenv("C:\\python\\API Keys and Such.env")

DRIVER = Service("C:\\python\\development\\geckodriver.exe")
PASSWORD = (os.environ.get("LinkedIn_Password"))
PHONE = "blergh"

# Opens a LinkedIn window. Alerts the user if the connection is made or not
browser = webdriver.Firefox(service=DRIVER)
try:
    logging.info("Attempting to make connection with website")
    browser.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C2&f_WT=2&geoId=101630962&keywords=python"
                "&location=Virginia%2C%20United%20States")
    logging.info("Connection successful")
except ConnectionError:
    logging.warning("Unable to make connection")

# Find and click the Sign-In button
logging.debug("Navigating to login page")
browser.find_element(By.CLASS_NAME, "nav__button-secondary").click()
time.sleep(3)

# Enter login information and submit
logging.debug("Navigation successful")
logging.debug("Entering login information")
browser.find_element(By.ID, "username").send_keys("nathan.hallberg@gmail.com")
browser.find_element(By.ID, "password").send_keys(PASSWORD)
browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
logging.debug("Information entered successfully")
time.sleep(3)

# Finds all the job listings
jobs = browser.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

# Loops through all the jobs
logging.info("Selecting first job listing")
for listing in jobs:
    listing.click()
    time.sleep(2)
    try:
        # Finds and clicks on the Easy Apply button
        browser.find_element(By.CLASS_NAME, "jobs-apply-button").click()
        time.sleep(2)
        # Attempts to clear and fill the phone number box
        phone = browser.find_element(By.ID, "urn:li:fs_easyApplyFormElement")
        phone.click()
        phone.clear()
        phone.send_keys(PHONE)
        try:
            # Attempts to click the "Follow Company" checkbox, unfollowing them
            browser.find_element(By.CSS_SELECTOR, "[for='follow-company-checkbox']").click()
        except NoSuchElementException:
            logging.info("No follow company checkbox")
        try:
            # Attempts to click on the "Submit application" button. Failing that, exits the application
            browser.find_element(By.CSS_SELECTOR, "[aria-label='Submit application']").click()
        except NoSuchElementException:
            logging.info("Submit application button not found. Exiting application")
    except NoSuchElementException:
        logging.info("Already applied to current position. Moving to the next")
    try:
        # Attempts to close current application. If application already complete, moves on
        browser.find_element(By.CSS_SELECTOR, '[aria-label="Dismiss"]').click()
        browser.find_element(By.CSS_SELECTOR, '[data-control-name="discard_application_confirm_btn"]').click()
    except ElementNotInteractableException:
        logging.info("Attempted to close application. No application to close")
    logging.info("Selecting next job listing")
    time.sleep(2)

browser.quit()