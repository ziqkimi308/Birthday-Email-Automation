# Birthday Email Automation

- This Python script automates the process of sending personalized birthday wishes via email. The script checks if today's date matches any birthdays listed in a CSV file, and if so, sends a custom birthday message using a randomly selected letter template.

---

### How it Works?:

- Birthday Data:
  - The script reads a CSV file (birthdays.csv) containing people's names, email addresses, and birth dates (month and day).
- Check Today's Date:
  - The script checks if today's date matches any of the birthdays in the CSV file.
- Select Letter Template:
  - If there is a match, the script randomly selects one of three pre-written birthday letter templates from the letter_templates folder.
- Send Email:
  - The script sends an email to the birthday person with a personalized message (their name is inserted into the template) via Gmail's SMTP server.

---

### Consideration:

- This project uses pandas and smtplib modules.
- You can add/modify the birthday letter templates in letter_templates which suits your preference.
- You can add/modify the birthday person details in birthdays.csv
- Update the script with your email credentials. Replace MY_EMAIL and MY_PASSWORD with your own Gmail account credentials.

---

### Screenshots:

<img width="932" alt="image" src="https://github.com/user-attachments/assets/db627bde-4fc8-4778-9bf9-be756c01eb8d">
