#!/usr/bin/env python3

################################################################
# Helpers to support Gmail API script
################################################################

import datetime
from email.mime.text import MIMEText
import base64
import json
import logging
import logging.handlers
import os
import requests
import smtplib
import sys
import time
import urllib.parse
import urllib.request

def send_email(user, password, to, subject, body):
    
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject

    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(user, password)
    mailserver.sendmail(user, to, msg.as_string())
    mailserver.quit()
    
    return "completed"

def load_logging():

    # create path to log file, create logs dir if it doesn't exist
    current_path = os.path.dirname(os.path.realpath(__file__))

    date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    logname = "check_gmail_" + date + ".log"
    
    log_filename = f"{current_path}/logs/{logname}"

    if not os.path.exists(f"{current_path}/logs"):
        os.makedirs(f"{current_path}/logs")

    # import base logging module
    logger = logging.getLogger("")
    logger.setLevel(logging.DEBUG)

    # add handler
    handler = logging.handlers.RotatingFileHandler(
        log_filename, maxBytes=(1048576*5), backupCount=7
    )

    # set formatting
    formatter = logging.Formatter("%(asctime)s => %(levelname)s : %(message)s", datefmt='%Y-%m-%d %I:%M:%S %p')
    handler.setFormatter(formatter)

    # apply handler to default logger
    logger.addHandler(handler)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

    return None


def get_access_token(client_id, client_secret, refresh_token):
    """
    Uses a refresh token to get an access token
    if refresh token expires, follow https://blog.macuyiko.com/post/2016/how-to-send-html-mails-with-oauth2-and-gmail-in-python.html to set up again
    """

    request_url = "https://accounts.google.com/o/oauth2/token"
    payload = {}
    payload["client_id"] = client_id
    payload["client_secret"] = client_secret
    payload["refresh_token"] = refresh_token
    payload["grant_type"] = "refresh_token"
    r = (
        urllib.request.urlopen(
            request_url, urllib.parse.urlencode(payload).encode("UTF-8")
        )
        .read()
        .decode("UTF-8")
    )
    return json.loads(r)


def get_messages(access_token):
    """
    Will get messages for a user
    """
    url = f"https://www.googleapis.com/gmail/v1/users/me/messages?access_token={access_token}"
    headers = {"Content-Type": "application/json"}
    payload = {}
    r = requests.request("GET", url, headers=headers, data=payload)
    if r.status_code != 200:
        err_resp = (
            f"Status Code Details:\n"
            f"Status code returned: {r.status_code}\n"
            f"Headers sent: {r.headers}\n"
            f"Body sent: {payload}\n"
            f"API response: {r.json()}"
        )
        logging.error(err_resp)
    return r.json()

def get_single_email(id, access_token):
    """
    Will get messages for a user
    """
    url = f"https://www.googleapis.com/gmail/v1/users/me/messages/{id}?access_token={access_token}"
    headers = {"Content-Type": "application/json"}
    payload = {}
    r = requests.request("GET", url, headers=headers, data=payload)
    if r.status_code != 200:
        err_resp = (
            f"Status Code Details:\n"
            f"Status code returned: {r.status_code}\n"
            f"Headers sent: {r.headers}\n"
            f"Body sent: {payload}\n"
            f"API response: {r.json()}"
        )
        logging.error(err_resp)
    return r.json()

def trash_single_email(id, access_token):
    """
    Will get messages for a user
    """
    url = f"https://www.googleapis.com/gmail/v1/users/me/messages/{id}/trash?access_token={access_token}"
    headers = {"Content-Type": "application/json"}
    payload = {}
    r = requests.request("POST", url, headers=headers, data=payload)
    if r.status_code != 200:
        err_resp = (
            f"Status Code Details:\n"
            f"Status code returned: {r.status_code}\n"
            f"Headers sent: {r.headers}\n"
            f"Body sent: {payload}\n"
            f"API response: {r.json()}"
        )
        logging.error(err_resp)
    return r.json()

def read_message(message):

    return_data = {}
    payload = message['payload']
    parts = payload['parts']

    for part in parts:
        msg_parts = part['parts']
        
        for msg_part in msg_parts:
            part_id = msg_part['partId']
            
            if part_id == "0.0":
                data = msg_part['body']['data']
                email_bytes = bytes(str(data),encoding='utf-8')
                decoded = base64.urlsafe_b64decode(email_bytes).decode('utf-8')
                decoded_email = str(decoded)
                
                # Hypothetically, I have two credit cards, one for purchasing stuff and another for bills
                # The one for purchasing stuff ends in 9999 so we test for that
                # if it is the other one, it will match 'bills_cc'
                if decoded_email.find("9999") != -1:
                    return_data['card'] = 'buying_cc'
                else:
                    return_data['card'] = 'bills_cc'
                
                m_index = decoded_email.find("$")
                amount = decoded_email[(m_index + 1): (m_index + 8)]
                
                # will match $9900.65 or $10321.87 
                if amount.find("\n") != -1:
                    return_data['amount'] = amount.strip()
                    
                else:
                    return_data['amount'] = amount

            else:
                pass

    return return_data

def get_days_until_payday():
    '''
    Get the number of days until the first of the month using only the datetime module
    '''

    today = datetime.datetime.today()
    #today = datetime.date(2021,2,28)
    year = today.year
    month = today.month
    day = today.day

    if day == 1:
        days_until_payday = 0
    else:
        date1 = datetime.date(year, month, day) 
        
        next_month = int(month) + 1
        
        # if Dec, bump to next year
        if next_month > 12: 
            next_month = 1
            year = int(year) + 1
        else:
            pass

        date2 = datetime.date(year, next_month, 1)
        
        days_til_first = (date1 - date2).days
        days_til_first = abs(days_til_first)
        days_until_payday = days_til_first

    return days_until_payday