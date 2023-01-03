import time
import requests
import schedule
api_key = 'API_KEY'

def job():
    msg = 'Go workout!'
    requests.post('https://api.mynotifier.app', {
        "apiKey": api_key,  # This is your own private key
        "message": msg,  # Could be anything
        "description": "You need to work!",  # Optional
        "body": "",  # Optional
        "type": "info",  # info, error, warning or success
        "project": ""  # Optional. Project ids can be found in project tab <-
    })
    print("Send message")

schedule.every().day.at("7:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)