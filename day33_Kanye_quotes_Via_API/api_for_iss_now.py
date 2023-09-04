#http://open-notify.org/Open-Notify-API/ISS-Location-Now/
#http://api.open-notify.org/iss-now.json
#{"message": "success", "iss_position": {"latitude": "-49.9336", "longitude": "-114.2348"}, "timestamp": 1690461191}

import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
# This will display only the response code like below
#<Response [200]>
#1XX : HOLD ON something is happening not fine
#2XX : HERE YOU GO everything successfull
#3XX : GO AWAY you don't have permission to get this response
#4XX : YOU SCREWED UP does not exist
#5XX : I SCREWED UP server / website is down
print(response. status_code)
#404 # NOT FOUND
#https://www.webfx.com/web-development/glossary/http-status-codes/
if response.status_code == 404:
        raise Exception("Resource does not exist at ISS")
elif response.status_code == 401:
        raise Exception("You are not Authorized to access this data")

print(response.raise_for_status())
#To print the json data
data = response.json()
#data = response.json()["iss_position"]
print(data)
# To get the specific value
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
iss_position = (latitude, longitude)
print (latitude, longitude)
print (iss_position)
# Overview
# This is a simple api to return the current location of the ISS. It returns the current latitude and longitude of the space station with a unix timestamp for the time the location was valid. This API takes no inputs.

# Output
# JSON
# http://api.open-notify.org/iss-now.json

# {
#   "message": "success", 
#   "timestamp": UNIX_TIME_STAMP, 
#   "iss_position": {
#     "latitude": CURRENT_LATITUDE, 
#     "longitude": CURRENT_LONGITUDE
#   }
# }
# The data payload has a timestamp and an iss_position object with the latitude and longitude.

# JSONP
# Appending a callback request to the query string will return JSONP:

# http://api.open-notify.org/iss-now.json?callback=CALLBACK

# CALLBACK({
#   "message": "success", 
#   "timestamp": UNIX_TIME_STAMP,
#   "iss_position": {
#     "latitude": CURRENT_LATITUDE, 
#     "longitude": CURRENT_LONGITUDE
#   }
# })