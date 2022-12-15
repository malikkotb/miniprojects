from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

with open('chrome_driver_path.txt') as file:
    chrome_driver_path = temp = file.read().splitlines()[0]

serv = Service(chrome_driver_path)
driver = webdriver.Chrome(service=serv)
URL = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)

t_end = time.time() + 60*5
while time.time() < t_end:
    money = int(driver.find_element(By.ID, 'money').text)
    print("\nMoney:", money)
    cookie = driver.find_element(By.ID, 'cookie')

    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()

    prices = {}

    cursor = driver.find_element(By.ID, 'buyCursor')
    cursor_price = cursor.find_element(By.TAG_NAME, 'b').text.split(' - ')[1].replace(',', '')
    prices['buyCursor'] = cursor_price

    grandma = driver.find_element(By.ID, 'buyGrandma')
    grandma_price = grandma.find_element(By.TAG_NAME, 'b').text.split(' - ')[1].replace(',', '')
    prices['buyGrandma'] = grandma_price


    factory = driver.find_element(By.ID, 'buyFactory')
    factory_price = factory.find_element(By.TAG_NAME, 'b').text.split(' - ')[1].replace(',', '')
    prices['buyFactory'] = factory_price


    mine = driver.find_element(By.ID, 'buyMine')
    mine_price = mine.find_element(By.TAG_NAME, 'b').text.split(' - ')[1].replace(',', '')
    prices['buyMine'] = mine_price


    shipment = driver.find_element(By.ID, 'buyShipment')
    shipment_price = shipment.find_element(By.TAG_NAME, 'b').text.split(' - ')[1].replace(',', '')
    prices['buyShipment'] = shipment_price


    lab = driver.find_element(By.ID, 'buyAlchemy lab')
    lab_price = lab.find_element(By.TAG_NAME, 'b').text.split(' - ')[1].replace(',', '')
    prices['buyAlchemy lab'] = lab_price


    portal = driver.find_element(By.ID, 'buyPortal')
    portal_price = portal.find_element(By.TAG_NAME, 'b').text.split(' - ')[1].replace(',', '')
    prices['buyPortal'] = portal_price


    time_machine = driver.find_element(By.ID, 'buyTime machine')
    time_machine_price = time_machine.find_element(By.TAG_NAME, 'b').text.split(' - ')[1].replace(',', '')
    prices['buyTime machine'] = time_machine_price

    click_on = ""
    max = 0
    for key in prices:
        if int(prices[key]) <= money:
            max = int(prices[key])
            click_on = key

    print(f"max: {max}, click on: {click_on}")
    if len(click_on) > 0:
        click_this = driver.find_element(By.ID, click_on)
        click_this.click()

    time.sleep(5)

print(driver.find_element(By.ID, 'cps').text)  # cookies per seconds after 5 minutes
driver.quit()