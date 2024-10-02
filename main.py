##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import random
import smtplib

# --------------------------- TODAY'S DATE ---------------------------
today = dt.datetime.now()
current_year = today.year
current_month = today.month
current_day = today.day

# ---------------------- BIRTHDAY PERSON'S NAME ----------------------
data_frame = pandas.read_csv("birthdays.csv")
names_list = data_frame["name"].to_list
print(names_list)
print(data_frame)
filtered_months = data_frame[data_frame.month == 10]
filtered_days = filtered_months[filtered_months.day == 2]
filtered_name = filtered_days["name"].to_string()
filtered_email = filtered_days["email"].to_string()

print(filtered_name)
print(filtered_email)


def clean_string(uncleaned):
    filtered_string = []
    allowed_chars = set(" @.")
    for sign in uncleaned:
        if sign.isalpha() or sign in allowed_chars:
            filtered_string.append(sign)
    return "".join(filtered_string).strip()


final_name = clean_string(filtered_name)
final_email = clean_string(filtered_email)

print()
print(final_name)
print(final_email)

# ------------ BIRTHDAY-PERSONS NAME INTO A RANDOM LETTER ------------
random_letter = random.randint(1, 3)
with open(f"letter_templates/letter_{random_letter}.txt", "r") as letter_file:
    letter = letter_file.read()

letter = letter.replace("[NAME]", final_name)

print(letter)

# ------------------------ SEND EMAIL ------------------------
MY_GMAIL = "peter.stepanic@gmail.com"
MY_PASSWORD = "rduqhmkbprxdhgzk"


# if final_name.isalpha():
#     print(type(final_name))
#     print("imamo birthday boja")
#     print(final_name)
