import requests
from bs4 import BeautifulSoup
import smtplib

URL = "EXAMPLE_URL_TO_SCRAPE"
header = {
    'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
response = requests.get(URL, headers=header)
amazon_webpage = response.content

soup = BeautifulSoup(amazon_webpage, 'html.parser')

price = soup.find(name='span', class_='a-price-whole').getText().split(',')[0]

if int(price) < 100:
    print(price)
    my_email = "SENDER_EMAIL"
    password = "YOUR_APP_PASSWORD" # app password (GOOGLE'S new rules)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()# secure our connection to email server -> message will be encrypted
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="REVEIVER_EMAIL",
            msg=f"Subject:Price Alert {price} Euro\n\nPrice: {price}Buy Now!\nLink:\n{URL}")