import datetime as dt
import pandas
from random import randint
import smtplib

MY_EMAIL = "python100daysofcodetest@gmail.com"
PASSWORD = "iupgrpelxcqpynoy"

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    name_of_person = birthdays_dict[today]["name"]
    email_address = birthdays_dict[today]["email"]
    random_letter = randint(1, 3)

    with open(f"./letter_templates/letter_{random_letter}.txt", "r") as file:
        letter = file.read()
    birthday_letter = letter.replace("[NAME]", name_of_person)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email_address,
            msg=f"Subject:Happy Birthday!\n\n{birthday_letter}"
        )





