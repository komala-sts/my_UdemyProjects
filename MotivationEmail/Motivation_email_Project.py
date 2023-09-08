#Monday Motivation Project
import smtplib
import datetime as dt
import calendar
import random


MY_EMAIL = "my@gmail.com"
MY_PASSWORD = "password"

now = dt.datetime.now()
weekday = now.weekday()
dayname= calendar.day_name[weekday]
with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

#print(quote) 
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=["komalasts@gmail.com", "shiv.pcs@gmail.com", "pinkyjosh2@gmail.com"],
        msg=f"Subject:{dayname} Motivation Quote from Komal through PythonAnyWhere.com\n\n{quote}"
    )

