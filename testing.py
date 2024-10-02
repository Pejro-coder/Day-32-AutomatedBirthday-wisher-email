import smtplib
import datetime as dt
import random

# --------------------------DATE------------------------
date = dt.datetime.now()
day = date.day

# date_of_birth = dt.datetime(year=1991, month=6, day=25)
# print(date_of_birth)


# ---------------------CHOOSE QUOTE---------------------
with open("quotes.txt", "r") as data_file:
    data = data_file.readlines()

current_quote = random.choice(data)
if "-" in current_quote:
    current_quote = current_quote.replace("- ", "\n- ")
    print(current_quote)


# -----------------------SEND EMAIL---------------------
MY_GMAIL = "peter.stepanic@gmail.com"
MY_PASSWORD = "rduqhmkbprxdhgzk"
email_list = ["peropycoder321tozihneobstaja@yahoo.com"]


if day == 2:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_GMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_GMAIL,
            to_addrs=email_list,
            msg=f"Subject:Monday motivation\n\n{current_quote}")
