import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

course = input("What course would you like to search for? ")

chrome_driver_path = "/Users/malik/Library/Mobile Documents/com~apple~CloudDocs/Development/chromedriver"
serv = Service(chrome_driver_path)
driver = webdriver.Chrome(service=serv) # we create a Chrome driver to drive

URL = "https://www.udemy.com"

driver.get(URL) # open a webpage (browser window) using driver
time.sleep(3)
driver.implicitly_wait(3)
search = driver.find_element(By.CLASS_NAME, 'ud-search-form-autocomplete-input')
search.send_keys(course)
search.send_keys(Keys.ENTER)

price = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[4]/div/span[2]/span').text
sale_price = price.split(',')[0]
if int(sale_price) < 20:
    # send email with price alert
    pass

driver.quit() # will quit the entire program