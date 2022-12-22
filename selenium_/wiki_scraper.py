from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

topic = str(input("What would u like to know about?\n")).lower()

chrome_driver_path = "/Users/malik/Library/Mobile Documents/com~apple~CloudDocs/Development/chromedriver"
serv = Service(chrome_driver_path)
driver = webdriver.Chrome(service=serv)

URL = "https://en.wikipedia.org/wiki/"
query = "_".join(topic.split(' '))
driver.get(f"{URL}{query}")

description = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[2]')
print(description.text)

driver.quit() # will quit the entire program
