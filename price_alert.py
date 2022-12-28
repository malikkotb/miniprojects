import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def notify(title, message):
    # Sends a notification to your desktop with desired title and message.
    command = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    os.system(command)

# You can set the price threshold when you want to get notified-
def scrape(price_threshold):
    url = "https://www.apple.com/de/shop/buy-iphone"
    chrome_driver_path = "/Users/malik/Library/Mobile Documents/com~apple~CloudDocs/Development/chromedriver"
    serv = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=serv)  # we create a Chrome driver to drive
    driver.get(url)

    model_name = driver.find_element(By.XPATH,
                                     '//*[@id="shelf-1_section"]/div[2]/div[1]/div/div/div[1]/div/div/div/div[1]/h3').text.split(' und')[0]
    model_price = driver.find_element(By.XPATH,
                                      '//*[@id="shelf-1_section"]/div[2]/div[1]/div/div/div[1]/div/div/div/div[3]/div/div/div/div[1]/span[3]/span').text
    model_price = model_price.split(' ')[0].replace('.', '')
    driver.quit()

    if int(model_price) <= price_threshold:
        notify("Price Alert", f"The price of {model_name} now starts at: {model_price}€.")


scrape(1300)