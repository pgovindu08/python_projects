##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import pandas as pd
import datetime as dt
import random

birthdays = pd.read_csv("birthdays.csv")
birth_dict = birthdays.to_dict(orient="list")

print(birth_dict)

my_email = "pranavseshasai.govindu@gmail.com"
password = "ggcjtqdbuefxvvdy"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()

today_date = dt.datetime.now()
present_month = today_date.month
present_date = today_date.day

birthday_letters = []

with open("./letter_templates/letter_1.txt") as letter1, open("./letter_templates/letter_2.txt") as letter2, open("./letter_templates/letter_3.txt") as letter3:
    birthday_letters.append(letter1.read())
    birthday_letters.append(letter2.read())
    birthday_letters.append(letter3.read())

with open("birthday_text.txt", "w") as file:
    random_letter = random.choice(birthday_letters)
    file.write(random_letter)

with open("birthday_text.txt") as file:
    letter_content = file.read()

for index, row in birthdays.iterrows():
    if row["month"] == present_month and row["day"] == present_date:
        name = row["name"]
        striped_name = name.strip()
        new_letters = letter_content.replace("[NAME]", striped_name)
        with open("birthday_text.txt", "w") as file:
            file.write(new_letters)
        with open("birthday_text.txt") as file:
            birthday_card = file.read()
                
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=row["email"], 
            msg=f"Subject:Happy Birthday!!!!\n\n{birthday_card}"
        )
                
connection.close()




