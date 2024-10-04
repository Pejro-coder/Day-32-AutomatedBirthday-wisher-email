import datetime as dt
import pandas
import random
import smtplib

# ------------------------------ TODAY'S DATE ------------------------------
today = dt.datetime.now()
current_month = today.month
current_day = today.day

# ---------------------------- BIRTHDAY NAMES ------------------------------
data_frame = pandas.read_csv("birthdays.csv")
filtered_months = data_frame[data_frame.month == current_month]
filtered_days = filtered_months[filtered_months.day == current_day]

filtered_names = []
filtered_emails = []
for index, row in filtered_days.iterrows():
    filtered_names.append(row["name"])
    filtered_emails.append(row["email"])
print(f"Filtered names: {filtered_names}")
print(f"Filtered emails: {filtered_emails}")

if len(filtered_names) > 0:
    # --------------- BIRTHDAY-PERSONS NAME INTO A RANDOM LETTER ---------------
    final_letters = []
    for name in filtered_names:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as letter_file:
            letter = letter_file.read()
        letter = letter.replace("[NAME]", name)
        final_letters.append(letter)

    # ------------------------------- SEND EMAIL -------------------------------
    MY_GMAIL = "peter.stepanic@gmail.com"
    MY_PASSWORD = "eqae jdrg stmk xasl"

    for letter in final_letters:
        current_email = filtered_emails[final_letters.index(letter)]
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_GMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_GMAIL,
                to_addrs=current_email,
                msg=f"Subject: Happy birthday!\n\n{letter}"
            )
        print(f"SENDING EMAIL TO {current_email}")
else:
    print("No birthdays on this day.")
