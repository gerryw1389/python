#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import sys
from dotenv import load_dotenv
import os
import json

load_dotenv()

try:
    api_key = os.environ["API_KEY"]
except KeyError:
    print("Unable to get environmental variables")
except Exception as e:
    print("Generic catch: Unable to get environmental variables")
    print("Generic catch: " + str(e))
        
# funds = ["VFIFX", "VWUSX", "VTSAX", "BTCUSD"]

# for fund in funds:
#     url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={fund}&apikey={api_key}"
#     payload = {}
#     headers = {
#     'Content-Type': 'application/json',
#     }
#     r = requests.request("GET", url, headers=headers, data=payload)
#     print(r.text)


url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=BTCUSD&apikey={api_key}"
payload = {}
headers = {
    'Content-Type': 'application/json',
}
r = requests.request("GET", url, headers=headers, data=payload)
req = r.json()

## print whole req

# print(req)
# print(dir(req))

## dump to file system

# filename = 'req.json'
# with open(filename, 'w') as f:
#     json.dump(req, f)

## get all the keys and values
#print(req['Time Series (Daily)'])

## get just the keys
#print(req['Time Series (Daily)'].keys())

## sort them
keylist = list(req['Time Series (Daily)'].keys())
keylist.sort(reverse=True)

## give me just the top 5
print(keylist[0:5])


## print their values to make sure we got them
first_five_list = keylist[0:5]

for first_five in first_five_list:
    print(req['Time Series (Daily)'][first_five])