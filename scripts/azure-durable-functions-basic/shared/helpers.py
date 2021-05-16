#!/usr/bin/python3

##################################################
# Helper functions
#
# Ctrl+Shift+[    Fold (collapse) region  editor.fold
# Ctrl+Shift+]    Unfold (uncollapse) region  editor.unfold
# Ctrl+K Ctrl+[   Fold (collapse) all subregions  editor.foldRecursively
# Ctrl+K Ctrl+]   Unfold (uncollapse) all subregions  editor.unfoldRecursively
# Ctrl+K Ctrl+0   Fold (collapse) all regions editor.foldAll
# Ctrl+K Ctrl+J   Unfold (uncollapse) all regions
##################################################

### Request Module Functions Template:
# credentials
# \n
# headers = {}
# \n
# url
# \n
# payload
# \n
# r = requests.request("PUT", url, auth=(u, p), headers=headers, data=json.dumps(payload))
# if r.status_code != 200:
#     err_resp = f"Status Code Details:\n" \
#         f"Status code returned: {r.status_code}\n" \
#         f"Headers sent: {r.headers}\n" \
#         f"Body sent: {payload}\n" \
#         f"API response: {r.json()}"
#     logging.error(err_resp)

# return r

#local testing
# from dotenv import load_dotenv
# load_dotenv()

import sys
import os
import logging
import requests
import json
from datetime import datetime, timedelta
import time

def err_response(log_msg):
    '''
    Formats an error string to be sent as a response to the main function.
    
    Example of how to call from main():
    e = helpers.err_response("Posting Request to IDG resulted in ERROR_STARTING_APPROVAL")
    return func.HttpResponse(e, status_code=400)

    Older way without function in main():
    err_response = f"ERROR: An error occurred while attempting to verify table record => {str(e)}"
    errRspJson = json.dumps({"response": err_response })
    logging.error(f"Sending Response: {errRspJson}")
    return func.HttpResponse(errRspJson, status_code=400)
    '''
    err_msg = f"ERROR: {log_msg}"
    errRspJson = json.dumps({"response": err_msg })
    logging.error(f"Sending Response: {errRspJson}")
    return errRspJson

def import_creds():
    '''
    Gets secrets from Azure Keyvault as an application
    Secret values are stored in the Function App under Configuration
    
    Example of how to call from main():
    keyvault_creds = import_creds()
    logging.info(f"client_id: { keyvault_creds['client_id'] }")
    logging.info(f"client_secret: { keyvault_creds['client_secret'] }")
    logging.info(f"tenant: { keyvault_creds['tenant'] }")
    logging.info(f"vault_name: { keyvault_creds['vault_name'] }")
    '''

    try:
        creds = {}
        creds["client_id"] = os.environ["client_id"]
        creds["client_secret"] = os.environ["client_secret"]
        creds["tenant"] = os.environ["tenant"]
        creds["vault_name"] = os.environ["vault_name"]
    except KeyError:
        logging.error("Unable to get env vars")
    except Exception as e:
        logging.error(f"Generic Catch: {str(e)}")

    return creds


def get_oauth(tenant, client_id, client_secret):
    '''
    Gets an Oauth token from Graph API as an application
    See the scope in the payload where the application is scoped to just Key Vault
    
    Example of how to call from main():
    token = get_oauth( 
        tenant = keyvault_creds['tenant'], 
        client_id = keyvault_creds['client_id'], 
        client_secret = keyvault_creds['client_secret'] 
    )
    '''
    url = f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"
    payload = "grant_type=client_credentials"\
        f"&client_id={client_id}"\
        f"&client_secret={client_secret}"\
        "&scope=https%3A%2F%2Fvault.azure.net%2F.default"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.request("POST", url, headers=headers, data=payload)
    r = response.json()
    return r


def get_secret(token, vault_name, secret_name):
    '''
    Using an Oauth token, gets the latest version of a secret
    
    Example of how to call from main():
    secret = get_secret(
        token = token["access_token"], 
        vault_name = keyvault_creds['vault_name'],
        secret_name = 'test'
    )
    logging.info(f"Secret value is : {secret['value']}")
    '''
    # Gets the latest version of a secret
    url = f"https://{vault_name}.vault.azure.net/secrets/{secret_name}?api-version=7.1"

    # for a specific version of the secret, replace {version}
    # version = "aadsfasdfasdfasdf"
    # url = f"https://{vault_name}.vault.azure.net/secrets/test/{version}?api-version=7.1"

    payload = {}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.request("GET", url, headers=headers, data=payload)
    r = response.json()
    return r


def get_sn_username():
    '''
    Using a combination of get_oauth() and get_secret() functions, 
    This will get an oauth token and retrieve the latest version of a secret
    
    Example of how to call from main():
    sn_username = get_sn_username()
    logging.info(f"Secret value is : {sn_username}")
    '''
    keyvault_creds = import_creds()
    token = get_oauth(tenant=keyvault_creds['tenant'],
                      client_id=keyvault_creds['client_id'],
                      client_secret=keyvault_creds['client_secret'])
    secret = get_secret(token=token["access_token"],
                        vault_name=keyvault_creds['vault_name'],
                        secret_name='Service-Now-User')
    return secret['value']

