
##################################################
# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt


# This function is called when a request is sent from Service Now from a catalog item.
# This function follows the template: One permission per request.
# It expects a response in the format of: {"response": "SUCCESS: current_date"}
# It will parse the response into separate values for each side of the semicolon

# Example payload:
# {
#   "sysid": "489e0ab2dbc5a0500acb38f0ad961988",
#   "number": "REQ0269517",
#   "description": "some text"
# }

##################################################

import sys
import os
import logging
import azure.functions as func
import requests
import json
from datetime import datetime, timedelta
import time
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from shared import helpers


def main(payload: dict) -> dict:
    
    data = dict(payload)

    #region => Parse the input

    sys_id = data["sysid"]
    logging.info(f"Extracted Service Now SysID: {sys_id}")

    req_number = data["number"]
    logging.info(f"Extracted Request Number: {req_number}")

    description = data["description"]
    logging.info(f"Extracted Description: {description}")

    # Check to ensure each are populated with something
    try:
        if all(v is not None for v in [sys_id, req_number, description]):
            pass
        else:
            e = helpers.err_response(
                "One of the variables populated at this point has a value of None"
                )
            return e
            
    except NameError as name:
        e = helpers.err_response(
                f"One of the variables is missing which should be populated at this point => Error details: {name}"
                )
        return e
    except Exception as e:
        e = helpers.err_response(
                f"Unhandled exception: {str(e)}"
                )
        return e

    #endregion => Parse the input

    #region => Start the main function
    try:
        
        logging.info("==========Starting Step 1: Do something with these variables==========")

        # Script removed

        pastdate = datetime.now() + timedelta(days=0,  hours=-6, minutes=0)
        date = pastdate.strftime("%Y-%m-%d-%r")
        response = f"SUCCESS: {date}"
        rspJson = json.dumps({"response": response })
        logging.info(f"Sending Response: {rspJson}")
        return rspJson
        #endregion => Response
    except Exception as e:
        logging.info(f"Generic Catch: {str(e)}")