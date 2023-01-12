import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

print('Welcome to kleinanzeigen. We will generate a list of your desired purchase.\nIncluding Price and Title of Product')
plz = input("Enter your zip code please: ")
item = input("Enter name of product you want listings from: ")

chrome_driver_path = "/Users/malik/Library/Mobile Documents/com~apple~CloudDocs/Development/chromedriver"
serv = Service(chrome_driver_path)
driver = webdriver.Chrome(service=serv)

URL = "https://www.ebay-kleinanzeigen.de/"
driver.get(URL)

time.sleep(2)
search = driver.find_element(By.ID, 'site-search-query')
search.send_keys(item)
zip_code = driver.find_element(By.ID, 'site-search-area')
zip_code.send_keys(plz)
time.sleep(1)
cookie_accept = driver.find_element(By.ID, 'gdpr-banner-accept')
cookie_accept.click()
time.sleep(1)
search_button = driver.find_element(By.ID, 'site-search-submit')
search_button.click()
time.sleep(2)

list_dict = {}
listings = driver.find_element(By.ID, 'srchrslt-adtable').find_elements(By.CLASS_NAME, 'lazyload-item')
for li in listings:
    list_dict[li.find_element(By.CLASS_NAME, 'text-module-begin').text] = li.find_element(By.CLASS_NAME, 'aditem-main--middle--price-shipping--price').text.split(' €')[0]

with open('kleinanzeigen-listings.json', 'w') as outfile:
    json.dump(list_dict, outfile)

driver.quit()
