from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

#TODO: Add logging and try/excepts

DRIVER = Service("C:\python\development\geckodriver.exe")

browser = webdriver.Firefox(service=DRIVER)
browser.get("https://en.wikipedia.org/wiki/Main_Page")

interactions = browser.find_element(By.CSS_SELECTOR, '[title="Special:Statistics"]')

print(f"There are {interactions.text} articles on Wikipedia")

browser.quit()