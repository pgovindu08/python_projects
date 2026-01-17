import requests
import smtplib
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

api_key = os.environ.get("OMW_API_KEY")
LAT = 35.923649
LON = -86.867828

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_list = weather_data["list"]

for hour_data in weather_list:
    weather_id = hour_data["weather"][0]["id"]
    print(weather_id)
    if weather_id < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body="It's going to rain today. Remember to bring an umbrella",
            to="whatsapp:+16292441306"
        )
        print(message.status)
        break
        

    