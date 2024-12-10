"""
********************************************************************************
* Project Name:  Birthday Email Automation
* Description:   This Python script automates the process of sending personalized birthday wishes via email.
* Author:        ziqkimi308
* Created:       2024-12-10
* Updated:       2024-12-10
* Version:       1.0
********************************************************************************
"""

# IMPORT
import pandas
import datetime as dt
import random
import smtplib

# CONSTANT
CSV_BIRTHDAY_PATH = "./birthdays.csv"
MY_EMAIL = "sweetsugarpastry@gmail.com"
MY_PASSWORD = "rqaarmydmibkgzdl"

# datetime Class
today = dt.datetime.now()
# Create a tuple
today_tupple = (today.month, today.day)

# Read CSV
data = pandas.read_csv(CSV_BIRTHDAY_PATH)

# Create a dictionary. Prototype: dict = (key:value) for (index, row) in iterrows()
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tupple in birthday_dict:
	# Modify the letter with specific names
	birthday_person = birthday_dict[today_tupple]
	file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
	with open(file_path) as file:
		letter = file.read()
		# .replace() returns new modified string but does not modift original string
		letter = letter.replace("[NAME]", birthday_person["name"]) 

	# The part where we send the letter via email	
	with smtplib.SMTP("smtp.gmail.com", 587) as connection:
		connection.starttls()
		connection.login(MY_EMAIL, MY_PASSWORD)
		connection.sendmail(
			from_addr=MY_EMAIL,
			to_addrs=birthday_person["email"],
			msg=f"Subject:Happy Birthday!\n\n{letter}"
		)
