#!/usr/bin/env python3

################################################################
# Example of sending email from an '@outlook.com' account
# Tested and confirmed working 2021/01/10
################################################################


import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

try:
    email_user = os.environ["MAIL_USER"]
    email_password = os.environ["MAIL_PASSWORD"]
    email_to = os.environ["MAIL_RECEIVER"]
except KeyError:
    print("Unable to get environmental variables")
except Exception as e:
    print("Generic catch: Unable to get environmental variables")
    print("Generic catch: " + str(e))

def send_email(user, password, to):
      
   html = """\
   <html>
   <head>
   </head>
   <body>
   This is a sample body
   </body>
   </html>
   """
   msg = MIMEText(html, 'html')
   msg['Subject'] = 'Test message'

   mailserver = smtplib.SMTP('smtp.office365.com',587)
   mailserver.ehlo()
   mailserver.starttls()
   mailserver.login(user, password)
   mailserver.sendmail(user, to, msg.as_string())
   mailserver.quit()
   return "completed"

send = send_email(email_user, email_password, email_to)
print(send)