#!/usr/bin/env python3

################################################################
# Example of sending email from a '@gmail.com' account
# Tested and confirmed working 2021/01/10
# This does not work since all the tabs and newlines are ignored
# see 3 for working copy
################################################################

import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

try:
    email_user = os.environ["GMAIL_USER"]
    email_password = os.environ["GMAIL_PASSWORD"]
    email_to = os.environ["MAIL_RECEIVER"]
except KeyError:
    print("Unable to get environmental variables")
except Exception as e:
    print("Generic catch: Unable to get environmental variables")
    print("Generic catch: " + str(e))

def send_email(user, password, to):
      
   text = 'Gerry\nPlease see the following:\n1\tJan\n2\tFeb'
   
   html = """\
   <html>
    <head>
    </head>
        <body>
        <p style="color:#006400"><b>{}</b></p>
        </body>
   </html>
   """.format(text)
   msg = MIMEText(html, 'html')
   msg['Subject'] = 'Test message'

   mailserver = smtplib.SMTP('smtp.gmail.com',587)
   mailserver.ehlo()
   mailserver.starttls()
   mailserver.login(user, password)
   mailserver.sendmail(user, to, msg.as_string())
   mailserver.quit()
   return "completed"

send = send_email(email_user, email_password, email_to)
print(send)