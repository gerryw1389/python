#!/usr/bin/python3

################################################################
# Example of sending email, may need to be tested again because this didn't seem to work consistently
################################################################


import smtplib
from email.mime.text import MIMEText
import os

def send_email(strPassword):
      
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
   mailserver.login('fromAccount@domain.com', strPassword)
   mailserver.sendmail('fromAccount@domain.com','toAccount@domain.com',msg.as_string())
   mailserver.quit()


try:
   email = os.environ["EMAIL"]
except Exception as e:
   exit(1)

send_email(email)