import requests
from datetime import datetime

# response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (latitude,longitude)

# print(iss_position)

MY_LAT = 35.923649
MY_LONG = -86.867828

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_time = sunrise.split("T")[1].split(":")[0]
print(sunrise_time)

sunset_time = sunset.split("T")[1].split(":")[0]
print(sunset_time)

time_now = datetime.now()
print(time_now.hour)