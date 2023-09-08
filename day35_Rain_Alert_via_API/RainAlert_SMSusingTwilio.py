#Note! For the code to work you need to replace all the placeholders with
#Your own details. e.g. account_sid, lat/lon, from/to phone numbers.
#https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
import requests
from twilio.rest import Client
 
#pip install  twilio
# Twilio helps to Send an SMS message in Python via the REST API. To send an outgoing SMS message from your 
# Twilio account you'll need to make an HTTP POST to Twilio's Message resource. 
# Twilio's Python library helps you to create a new instance of the Message resource, 
# specifying the To, From, and Body parameters of your message.

#DO FREE SIGN IN TO GET API KEY FROM https://api.openweathermap.org
# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
#api_key = os.environ.get("OWM_API_KEY")
#https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=9bc70b8290780d7207f939d894b1f7a6
#https://api.openweathermap.org/data/2.5/weather?lat=53.48075&lon=-2.242631&appid=9bc70b8290780d7207f939d894b1f7a6&exclude=current%2Cminutely%2Cdaily
 
api_key = "Your API Key"
#FOR SENDING SMS
account_sid = "YOUR ACCOUNT SID"
auth_token = "YOUR Auth token"
 
# account_sid = "YOUR ACCOUNT SID"
# auth_token = os.environ.get("AUTH_TOKEN")
#Manchester/Coordinates 53.4808° N, 2.2426° W
#Manchester lat=53.480759  , long = -2.242631
weather_params = {
    "lat": "53.480759",
    "lon": "-2.242631",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["weather"]
print(weather_slice)
will_rain = False

for data in weather_slice:
    main_description = data["main"].lower() 
    #print(main_description)
    #print(main_description.find("rain"))
    if(main_description.find("rain") != -1):
        will_rain = True
         
print("will rainy: ", will_rain)
 
if will_rain:
    client = Client(account_sid, auth_token)
    #Twilio number +447360537525
    message = client.messages.create(
    from_="+447360537525",
    body="It's going to rain today. Remember to bring an ☔️",
    to='+447760510303')
    print(message.sid)
    print(message.status)





 
