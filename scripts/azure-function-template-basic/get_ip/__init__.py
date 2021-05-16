#!/usr/bin/python3

##################################################
# This function will return the public ip of the function app
# No input is needed for this function

##################################################

import sys
import logging
import azure.functions as func
import os
import time
from datetime import datetime, timedelta
import json
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:

    url = "https://ifconfig.me/ip"
    payload = {}
    headers = {
    'Content-Type': 'application/json',
    }
    r = requests.request("GET", url, headers=headers, data=payload)
        
    response = r.text
    logging.info(f"Response: {response}")

    ### Response
    pastdate = datetime.now() + timedelta(days=0,  hours=-6, minutes=0)
    date = pastdate.strftime("%Y-%m-%d-%r")
    
    rspJson = json.dumps([{ 
            "response": response,
            "date_time": date 
    }])
    return func.HttpResponse(rspJson, status_code=200)

if __name__ == '__main__':
    main(req)
else:
    logging.error("Function not called correctly, please try again.")