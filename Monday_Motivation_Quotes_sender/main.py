import datetime as dt
import random
import smtplib

my_email = "pranavseshasai.govindu@gmail.com"
password = "ggcjtqdbuefxvvdy"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()


with open("quotes.txt") as date_file:
    quotes = date_file.readlines()
random_quote = random.choice(quotes)

now = dt.datetime.now()
week_day = now.weekday()

if week_day == 6:
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="pssg2103@gmail.com", 
        msg=f"Subject:Motivation Quote\n\n{random_quote}"
    )
    connection.close()
