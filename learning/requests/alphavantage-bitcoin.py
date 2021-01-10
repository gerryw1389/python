#!/usr/bin/env python3

################################################################
# Example of using AlphaVantage API
# Sign up to get an API key and import it
# This script currently just gets the 5 latest values for bitcoin but can do others as well
# will eventually replace my powershell script at https://automationadmin.com/2020/09/ps-send-email-bitcoin
################################################################

import requests
from requests.auth import HTTPBasicAuth
import sys
from dotenv import load_dotenv
import os
import json
import math

load_dotenv()

try:
    api_key = os.environ["API_KEY"]
except KeyError:
    print("Unable to get environmental variables")
except Exception as e:
    print("Generic catch: Unable to get environmental variables")
    print("Generic catch: " + str(e))

url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey={api_key}"
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
keylist = list(req['Time Series (Digital Currency Daily)'].keys())
keylist.sort(reverse=True)

## give me just the top 5
# print(keylist[0:5])


## print their values to make sure we got them
first_five_list = keylist[0:5]
# print(type(first_five_list))

# # Print the closing price last 5 days
# for first_five in first_five_list:
#     #print(req['Time Series (Digital Currency Daily)'][first_five])
#     print(req['Time Series (Digital Currency Daily)'][first_five]['4b. close (USD)'])

#     '''
#     prints:
#     40485.86000000
#     40088.22000000
#     40582.81000000
#     39432.28000000
#     36769.36000000
#     '''

# for first_five in first_five_list:
#     key = first_five
#     value = req['Time Series (Digital Currency Daily)'][first_five]
#     close = value['4b. close (USD)']
#     print(f"{key} : {close}")
    #     '''
#     prints:
    # 2021-01-10 : 40485.86000000
    # 2021-01-09 : 40088.22000000
    # 2021-01-08 : 40582.81000000
    # 2021-01-07 : 39432.28000000
    # 2021-01-06 : 36769.36000000
#     '''

# now that we see the top five, store in variables for comparisons
first_key = first_five_list[0]
first_value = req['Time Series (Digital Currency Daily)'][first_key]['4b. close (USD)']
first_value = math.floor(float(first_value))

second_key = first_five_list[1]
second_value = req['Time Series (Digital Currency Daily)'][second_key]['4b. close (USD)']
second_value = math.floor(float(second_value))


third_key = first_five_list[2]
third_value = req['Time Series (Digital Currency Daily)'][third_key]['4b. close (USD)']
third_value = math.floor(float(third_value))

fourth_key = first_five_list[3]
fourth_value = req['Time Series (Digital Currency Daily)'][fourth_key]['4b. close (USD)']
fourth_value = math.floor(float(fourth_value))

fifth_key = first_five_list[4]
fifth_value = req['Time Series (Digital Currency Daily)'][fifth_key]['4b. close (USD)']
fifth_value = math.floor(float(fifth_value))

print(f"{first_key}: {first_value}")
print(f"{second_key}: {second_value}")
print(f"{third_key}: {third_value}")
print(f"{fourth_key}: {fourth_value}")
print(f"{fifth_key}: {fifth_value}")

# now compare
# if first_value < second_value:
#     print("First is less than second")
# else:
#     print("First is greater than second")

# if first_value < second_value < third_value:
#     print("First is less than second and third")
# else:
#     print("First is greater than second and third")

# if we want to see if it is on a 5 day trend upwards
# if first_value > second_value > third_value > fourth_value > fifth_value:
#     print("Trend is upwards for five days straight")
# else:
#     print("Trend is not upwards for five days straight")

# # if we want to see if it is on a 5 day trend downwards
# if first_value < second_value < third_value < fourth_value < fifth_value:
#     print("Trend is downwards for five days straight")
# else:
#     print("Trend is not downwards for five days straight")

# print(first_value / second_value)

if first_value < second_value < third_value :
    print("Trend is downwards for three days straight")
    # Here I will send an email to buy if down for 3 days straight
else:
    print("Trend is not downwards for three days straight")