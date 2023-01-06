import requests
from twilio.rest import Client


account_sid = "account_sid"
auth_token = "auth_token"
api_key = "api_key"
OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 48.131240,
    "lon": 11.599037,
    "appid": api_key,
    "units": "metric",
}


#if ID < 700: bring umbrella
# if code is between 700 and 782 -> there is some type atmosepheric stuff going on
# if code = 800 -> Clear sky
# if code > 800 -> clouds

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
day_forecast = [data['list'][i]['weather'][0]['id'] for i in range(3)] # get id code for first 4 measures per day


will_rain = False
text = "It's not gonna rain today 🤗"
# check for rain with id-weather-code
for i in day_forecast:
    if int(i) < 700:
        print(i)
        text = "It's going to rain today. Remember to bring an ☔️"

client = Client(account_sid, auth_token)
message = client.messages.create(
    body=text,
    from_="+18304654451",
    to='+4917643476680'
)
print(message.status)
