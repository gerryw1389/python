#!/usr/bin/python3

##################################################
# This function will return a parsed description from a passed in string
# {
#    "description": "something"
# }
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

    req_body = req.get_json()

    description = req_body["description"]
    logging.info(f"Extracted description: {description}")

    splitDesc = description.split("\n")
    
    split_list = [x.strip() for x in splitDesc[8].split(":")[1].split(',')]
    logging.info(f"Extracted split list: {split_list}")

    department = splitDesc[3].split(":")[1].strip()
    logging.info(f"Extracted department: {department}")

    split_list_string = ','.join(split_list)

    ### Response
    pastdate = datetime.now() + timedelta(days=0,  hours=-6, minutes=0)
    date = pastdate.strftime("%Y-%m-%d-%r")
    

    rspJson = json.dumps([{ 
            "serial_numbers": split_list_string,
            "department": department,
            "date_time": date 
    }])
    return func.HttpResponse(rspJson, status_code=200)

if __name__ == '__main__':
    main(req)
else:
    logging.error("Function not called correctly, please try again.")