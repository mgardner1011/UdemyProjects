import requests
from twilio.rest import Client

account_sid = 'Twilio_api_sid'
auth_token = 'twilio_auth_token'

base_url = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {
    'lat': 51.500149,
    'lon': -0.126240,
    'cnt': 4,
    'appid': 'owm_api_key',
}

response = requests.get(base_url, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in range(len(weather_data['list'])):
    condition_code = weather_data['list'][hour_data]['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella ☔",
        from_='+19257226085',
        to='+15027776346'
    )
    print(message.status)
