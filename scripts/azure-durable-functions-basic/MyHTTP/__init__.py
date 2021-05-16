# This function an HTTP starter function for Durable Functions.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable activity function (default name is "Hello")
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import azure.functions as func
import azure.durable_functions as df

async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    
    req_body = req.get_json()

    description = req_body["description"]
    logging.info(f"Extracted Description: {description}")

    req_number = req_body["number"]
    logging.info(f"Extracted Request Number: {req_number}")

    sys_id = req_body["sysid"]
    logging.info(f"Extracted Service Now SysID: {sys_id}")

    payload = {
        "description": description,
        "number": req_number,
        "sysid": sys_id
    }

    logging.info("Starting Async Orchestration for MyOrch...")
    logging.info(f"Sending payload to Orchestrator Function extracted from input: {payload}")

    client = df.DurableOrchestrationClient(starter)
    instance_id = await client.start_new('MyOrch', None, payload )

    logging.info(f"Started orchestration with ID = '{instance_id}'.")

    return client.create_check_status_response(req, instance_id)