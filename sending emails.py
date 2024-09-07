import smtplib

"""
Before @ is the identity of my email, and after is identity of email
email provider. These will change based on email provider.
"""
# email = #your email
# password = # your password


"""
Create object from this class. If your email is @gmail.com, then the following
Is how you'd connect to your email server.
"""
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()   # Transport Layer Security - layers security, encrypts the message, secures connection
# connection.login(user=email, password=password)
# # connection.sendmail(from=<your email>, to_address=<type email>, msg=<type message>)
# by typing "Subject:<subject line>\n\n<body>
# connection.close()    instead of using this we can:
#with smtplib.SMTP("smtp.gmail.com") as connection: Then indented the rest.

"""
1. check for typos
2. follow error code URL
3. URL > Profile > Manage Google Account > Security > 2-step Verification > Turn On > Security > 
App Passwords > Login > Select App > Birthday Wisher > Copy App Password > Paste into password

"""