##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas

today = dt.datetime.now()
current_year = today.year
current_month = today.month
current_day = today.day

# with open("birthdays.csv", "r") as data_file:
#     birthdays = data_file.read()
#     print(birthdays)

df = pandas.read_csv("birthdays.csv")
print(df)
month_list = df["month"].to_list()
day_list = df["day"].to_list()
print(month_list)
print(day_list)
#
# for month in month_list:
#     if month == current_month:
#         print(month_list.index(month))

print(df["day"])

