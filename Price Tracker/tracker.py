import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


#TODO: Make a GUI to enter an amazon URL into

URL = "https://www.amazon.com/dp/125016026X/?coliid=I9TJUK7U5CQK7&colid=2MMGC4MX4VHIP&psc=1&ref_=lv_ov_lig_dp_it"
DRIVER = Service(r"C:\python\development\geckodriver.exe")
amazon = webdriver.Firefox(service=DRIVER)

try:
    logging.info("Attempting to connect with website")
    amazon.get(URL)
    logging.info("Successfully made connection")
except ConnectionError:
    logging.warning("Unable to make connection with website")

logging.debug("Attempting to find price")
current_price = float(amazon.find_element(By.CSS_SELECTOR, "[data-feature-name='corePrice']").text.strip("$"))
amazon.close()

camel = webdriver.Firefox(service=DRIVER)
try:
    logging.info("Attempting to connect with website")
    camel.get("https://camelcamelcamel.com/")
    logging.info("Successfully made connection")
except ConnectionError:
    logging.warning("Unable to make connection with website")

camel.find_element(By.ID, "sq").send_keys(URL)
camel.find_element(By.ID, "sqbtn").click()

highest_price = float(camel.find_element(By.CLASS_NAME, "highest_price").text.split(" ")[2].strip("$"))
lowest_price = float(camel.find_element(By.CLASS_NAME, "lowest_price").text.split(" ")[2].strip("$"))
maximum_price = highest_price-((highest_price-lowest_price)/2)

camel.close()

if current_price <= maximum_price:
    print("Get it! It's a pretty good price!")
else:
    print("Future unclear. Ask again later.")