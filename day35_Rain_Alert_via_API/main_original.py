#Note! For the code to work you need to replace all the placeholders with
#Your own details. e.g. account_sid, lat/lon, from/to phone numbers.
#https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
#pip install  twilio
# Twilio helps to Send an SMS message in Python via the REST API. To send an outgoing SMS message from your 
# Twilio account you'll need to make an HTTP POST to Twilio's Message resource. 
# Twilio's Python library helps you to create a new instance of the Message resource, 
# specifying the To, From, and Body parameters of your message.

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
#api_key = os.environ.get("OWM_API_KEY")
api_key = os.environ.get("9bc70b8290780d7207f939d894b1f7a6")
account_sid = "YOUR ACCOUNT SID"
auth_token = os.environ.get("AUTH_TOKEN")
#Manchester lat=53.480759  , long = -2.242631
weather_params = {
    "lat": "YOUR LATITUDE",
    "lon": "YOUR LONGITUDE",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)
