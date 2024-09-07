import smtplib
import random
from datetime import datetime
import pandas

# Open Each Letter
with open("./letter_templates/letter_1.txt", "r") as data_1:
    letter_1 = data_1.read()
with open("./letter_templates/letter_2.txt") as data_2:
    letter_2 = data_2.read()
with open("./letter_templates/letter_3.txt") as data_3:
    letter_3 = data_3.read()

# Open & Read csv, Replace '[NAME]' With Name
bday_file = pandas.read_csv("./birthdays.csv")
for name in bday_file["name"]:
    new_letter_1 = letter_1.replace("[NAME]", name)
    new_letter_2 = letter_2.replace("[NAME]", name)
    new_letter_3 = letter_3.replace("[NAME]", name)

# Random Letter
random_letters = [new_letter_1, new_letter_2, new_letter_3]
random_letter = random.choice(random_letters)

# Check Email Sent On Today's Date (Test)
today = datetime.now()
birthday_tuple = (today.month, today.day)
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in bday_file.iterrows()}
if birthday_tuple in birthday_dict:
    # Send Email With Randomised Letter
    sender_email = " "      # Enter your email
    sender_password = " "   # Passkey found with your email provider
    recipient_email = " "   # recipient email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()   # Secure Connection
        connection.login(user=sender_email, password=sender_password)  # Login
        connection.sendmail(from_addr=sender_email,
                            to_addrs=recipient_email,
                            msg="Subject:Happy Birthday!!\n\n"f"{random_letter}")
        connection.close()  # Closes Connection
