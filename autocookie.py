import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

# TODO: Add logging and try/excepts
#       Save session on close
#           Write save link to txt

DRIVER = Service(r"C:\python\development\geckodriver.exe")

browser = webdriver.Firefox(service=DRIVER)
logging.info("Attempting to connect with website")
try:
    browser.get("http://orteil.dashnet.org/experiments/cookie/")
except RuntimeError:
    print("Unable to form connection with website")

cookie = browser.find_element(By.ID, "cookie")
store = browser.find_elements(By.CSS_SELECTOR, "#store div")
items = [item.get_attribute("id") for item in store]

timeout = time.time() + 5

while True:
    cookie.click()
    if time.time() > timeout:
        money = int(browser.find_element(By.ID, "money").text.replace(",", ""))
        all_prices = browser.find_elements(By.CSS_SELECTOR, "#store b")
        prices = []
        # Finds the current price of all the items
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(str(element_text.split("-")[1]).strip().replace(",", ""))
                prices.append(cost)
        # Create a dictionary of items and prices
        cookie_upgrades = {}
        for n in range(len(prices)):
            cookie_upgrades[items[n]] = prices[n]
        # Find upgrades you can afford
        affordable_upgrades = {}
        for title, cost in cookie_upgrades.items():
            if money > cost:
                affordable_upgrades[title] = cost
        # Find and buy the highest price item
        if affordable_upgrades == {}:
            continue
        else:
            highest_price = max(affordable_upgrades, key=affordable_upgrades.get)
        to_purchase = affordable_upgrades[highest_price]
        browser.find_element(By.ID, highest_price).click()
        timeout = time.time() + 5
