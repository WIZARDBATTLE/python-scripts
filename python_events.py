from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

#TODO: Add logging and try/excepts
#      Make the output more user friendly and easier to read


DRIVER = Service("C:\python\development\geckodriver.exe")

browser = webdriver.Firefox(service=DRIVER)
browser.get("https://www.python.org/")

events_list = browser.find_element(By.CSS_SELECTOR, '[class="medium-widget event-widget last"]')
event_times = events_list.find_elements(By.TAG_NAME, "time")
event_names = events_list.find_elements(By.TAG_NAME, "li a")
events = {}


for n in range(len(event_names)):
    events[n] = {
        "time": event_times[n].text,
        "event": event_names[n].text
    }

print(events)

browser.quit()