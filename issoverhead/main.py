import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 35.923649 # Your latitude
MY_LONG = -86.867828 # Your longitude

#Your position is within +5 or -5 degrees of the ISS position.
def in_range():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    high_limit_lat = MY_LAT+5
    low_limit_lat = MY_LAT-5
    high_limit_long = MY_LONG+5
    low_limit_long = MY_LONG-5
    if iss_latitude <= high_limit_lat and iss_latitude >= low_limit_lat and iss_longitude <= high_limit_long and iss_longitude >= low_limit_long:
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = int(time_now.hour)

def is_dark():
    if hour >= sunset or hour <= sunrise:
        return True
    else:
        return False


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if in_range() and is_dark():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user="pranavseshasai.govindu@gmail.com", password="ggcjtqdbuefxvvdy")
            connection.sendmail(
            from_addr="pranavseshasai.govindu@gmail.com",
            to_addrs="pssg2103@gmail.com",
            msg="Subject: ISS Overhead\n\nLook up! The ISS is above you in the sky!"
        )
    