import random
import smtplib
import datetime as dt

"""
Send a motivation quote via email on the current weekday (now)
change it to Monday later.
"""

# TODO List
# TODO - Remove \n, Replace \ with ',
# 1. Setup email connection (done)
# 2. Open up file (either using pandas or normally) (done)
# 3. Convert quotes into a list (done)
# 4. Randomly choose any quote  (done)
# 5. Setup date & time of sending (done)
# 5. Import as msg and send email as a test (done)
# 6. Change day of week to sent on Mondays (optional)

now = dt.datetime.now()
weekday = now.weekday()     # The weekday = current weekday (now.weekday())
if weekday == 4:    # Thursday; Monday(0), Tuesday(1), etc.
    with open("./quotes.txt") as data:  # Open file, convert to list
        # file = data so, data.readlines() converts into a list. When opening files, we can use methods for that file.
        all_quotes = data.readlines()
        quote = random.choice(all_quotes)
        print(quote)

    sender_email = " "      # Enter your email
    sender_password = " "   # Passkey found with your email provider
    recipient_email = " "   # recipient email

    with smtplib.SMTP("smtp.gmail.com") as connection:  # Same as connection (var) = smtplib.SMTP(xyz.gmail.com)
        connection.starttls()   # secure connection
        connection.login(user=sender_email, password=sender_password)   # Login
        connection.sendmail(from_addr=sender_email,
                            to_addrs=recipient_email,
                            msg="Subject:Motivation For You!\n\n"f"{quote}")   # This format to + Subject & Body
        connection.close()
