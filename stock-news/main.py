from pprint import pprint
from twilio.rest import Client
from datetime import date
from datetime import timedelta
import requests
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
stock_api_key = 'dtock_api_key' #alpha vantage api keye
news_api_key = 'news_api_key'
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': stock_api_key,
}
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = response.json()['Time Series (Daily)']
today = date.today()
yesterday = today - timedelta(days=1)
yesterday_closing = data[str(yesterday)]['4. close']
print(yesterday_closing)

vorgestern = today - timedelta(days=2)
vorgestern_closing = data[str(vorgestern)]['4. close']
print(vorgestern_closing)

difference = abs(float(yesterday_closing) - float(vorgestern_closing))
print(difference)

diff_percent = (difference / float(yesterday_closing)) * 100
print(diff_percent)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
top_articles = []
if diff_percent > 5:
    news_params = {
        "apiKey": news_api_key,
        "qInTitle": STOCK,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']
    top_articles = articles[:3]
    #pprint(top_articles)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

account_sid = "account_sid" # from twilio
auth_token = "auth_token"

message_list = []
for i in range(len(top_articles)):
    article = f"Headline: {top_articles[i]['title']}\nBrief: {top_articles[i]['description']}\n\n"
    message_list.append(article)

#[print(i) for i in message_list]
text = "".join(message_list)

client = Client(account_sid, auth_token)
message = client.messages.create(
    body=text,
    from_="+18304654451",
    to='+4917643476680'
)
print(message.status)

