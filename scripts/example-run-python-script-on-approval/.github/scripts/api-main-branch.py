#!/usr/bin/python3

##################################################
# This function will call API Mgmt to run a script on a remote server
##################################################

import sys
import os
import json
import requests


def main():

    try:
        api_key = os.environ["api_key"]
    except KeyError:
        print("unable to get env vars")
    except Exception as e:
        print("Generic Catch: unable to get env vars")
        print(str(e))

    url = "https://my-api.azure-api.net/my-prod-function-app/my-prod-function"

    payload = json.dumps(
        {
            "hostname": "myserver.domain.com",
            "script_path": "/home/me/scripts/sync-repo.sh",
        }
    )

    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": api_key,
        "Ocp-Apim-Trace": "true",
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


if __name__ == "__main__":
    main()
else:
    print("Function not called correctly, please try again.")