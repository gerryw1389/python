# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):

    input = context.get_input()
    payload = dict(input)
    
    logging.info("Extracting information from payload for MyActivity....")
    logging.info(f"Sending payload to Activity Function extracted from HTTP: {payload}")

    result = yield context.call_activity('MyActivity', payload)
    
    logging.info("Completed Async Orchestration")
    
    return [result]

main = df.Orchestrator.create(orchestrator_function)