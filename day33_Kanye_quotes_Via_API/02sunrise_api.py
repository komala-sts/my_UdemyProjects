#https://sunrise-sunset.org/api#
#https://api.sunrise-sunset.org/json
#{"results":{"sunrise":"6:01:54 AM","sunset":"6:11:11 PM","solar_noon":"12:06:33 PM","day_length":"12:09:17","civil_twilight_begin":"5:41:08 AM","civil_twilight_end":"6:31:58 PM","nautical_twilight_begin":"5:15:40 AM","nautical_twilight_end":"6:57:25 PM","astronomical_twilight_begin":"4:50:09 AM","astronomical_twilight_end":"7:22:57 PM"},"status":"OK"}

# https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400
#response is
# // 20230728111542
# // https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400

# {
#   "results": {
#     "sunrise": "5:18:47 AM",
#     "sunset": "7:29:38 PM",
#     "solar_noon": "12:24:13 PM",
#     "day_length": "14:10:51",
#     "civil_twilight_begin": "4:51:20 AM",
#     "civil_twilight_end": "7:57:05 PM",
#     "nautical_twilight_begin": "4:16:01 AM",
#     "nautical_twilight_end": "8:32:24 PM",
#     "astronomical_twilight_begin": "3:37:47 AM",
#     "astronomical_twilight_end": "9:10:38 PM"
#   },
#   "status": "OK"
# }

# https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=today

# https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=2023-07-14

# https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&formatted=0

import requests
import datetime

# parameters latitude and longitude of LONDON city for sunrise API
MY_LAT = 53.487 #51.507351
MY_LONG = -2.2901 #-0.127758
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
   
}
#
#4:16:09 AM 8:15:14 PM 15:59:05
#when "formatted": 0 in the parameters we ge t below data which could be split and shown for 24hr format
#2023-07-28T04:16:09+00:00 2023-07-28T20:15:14+00:00 57545

# "formatted": 0 to return in 24 hr format instead of 12 hr format
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
#below is the actual execution command
response.raise_for_status()
data = response.json()
print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
daylength = data["results"]["day_length"]
print(sunrise, sunset, daylength)
##when "formatted": 0
#2023-07-28T04:16:09+00:00 
# #2023-07-28T20:15:14+00:00 
# 357545
sunrise_hr = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hr = data["results"]["sunset"].split("T")[1].split(":")[0]

print("Sunrise Hour" , sunrise_hr)
print("Sunset Hour" , sunset_hr)

