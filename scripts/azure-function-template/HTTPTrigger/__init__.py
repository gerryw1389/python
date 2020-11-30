import logging
import azure.functions as func
from . import helpers


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.warning("Python HTTP trigger function processed a request.")

    # Show request info
    logging.warning("Request body: {}".format(req))

    req_body = req.get_json()
    logging.warning("Request body as json: {}".format(req_body))

    # Assuming the information is passed in payload:

    #name = req.params.get("name")
    name = req_body.get("name")
    logging.warning("Extracted name: {}".format(name))

    #car = req.params.get("car")
    car = req_body.get("car")
    logging.warning("Extracted car: {}".format(car))

    city = req_body.get('birth', {}).get('city')
    logging.warning("Extracted city: {}".format(city))

    state = req_body.get('birth', {}).get('state')
    logging.warning("Extracted state: {}".format(state))

    # Test calling other modules in the same dir
    one = helpers.helpers_test("one")
    logging.warning("imported module test - one: {}".format(one))

    two = helpers.helpers_test("")
    logging.warning("imported module test - two: {}".format(two))

    # Finally, return the response
    response = "Hello, {}.\n\nYou chose {}.\n\nYour birth city is {} in the state of {}".format(
        name, car, city, state)
    return func.HttpResponse(response, status_code=200)
