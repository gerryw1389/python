#!/usr/bin/python3

import sys
import logging
import azure.functions as func
from . import helpers
from shared import shared
import json
from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    logging.info("Called function ReadXML")

    # Show request info
    logging.info("Request body: {}".format(req))

    req_body = req.get_json()
    logging.info("Request body as json: {}".format(req_body))

    # Assuming the information is passed in payload:

    #name = req.params.get("name")
    name = req_body.get("name")
    logging.info("Extracted name: {}".format(name))

    #car = req.params.get("car")
    car = req_body.get("car")
    logging.info("Extracted car: {}".format(car))

    city = req_body.get('birth', {}).get('city')
    logging.info("Extracted city: {}".format(city))

    state = req_body.get('birth', {}).get('state')
    logging.info("Extracted state: {}".format(state))

    # Test calling other modules in the same dir
    one = helpers.helpers_test("one")
    logging.info("imported module test - one: {}".format(one))

    two = helpers.helpers_test("")
    logging.info("imported module test - two: {}".format(two))

    three = shared.shared_helpers_test("import shared one")
    logging.info("imported module shared - three: {}".format(three))

    # Finally, return the response
    
    response = "Hello, {}.\n\nYou chose {}.\n\nYour birth city is {} in the state of {}".format(
        name, car, city, state)

    rspJson = json.dumps([ {
    "response": response, 
    "date_time": date
    } ])

    err_response = "Please pass a name on the query string or in the request body"

    errRspJson = json.dumps([ {
    "response": err_response, 
    "date_time": date
    } ])
    
    if name and car and city and state:
        return func.HttpResponse(rspJson, status_code=200)
    else:
        return func.HttpResponse(errRspJson, status_code=400)

if __name__ == '__main__':
    main(req)
else:
    print("function not called correctly")