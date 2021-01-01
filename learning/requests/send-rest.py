#!/usr/bin/env python3

################################################################
# This is an example I have used to send a REST call to Azure Event Grid
################################################################

from datetime import datetime, timezone
import requests
import json
import collections

def send_req(subject, payload, key):

   date1 = datetime.now(timezone.utc)
   date2 = (str(date1).replace(" ", "T").replace("+00:00", "0")) + 'Z'

   # generate body
   body = collections.OrderedDict()
   body["body"] = payload

   # insert into main body
   data = collections.OrderedDict()
   data["id"] = "MyApp"
   data["subject"] = subject
   data["topic"] = "somePub"
   data["eventType"] = "MyAppApproval"
   data["eventTime"] = date2
   data["data"] = body
   data["dataVersion"] = "1.0"
   data["metadataVersion"] = None
   #print("data: ", data)

   headers = collections.OrderedDict()
   headers['Content-Type'] = 'application/json'
   headers['aeg-sas-key'] = key
   #print("headers: ", headers)

   data2 = "[" + json.dumps(data) + "]"
   #print("data string: ", data2)

   url = "https://mycompany.southcentralus-1.eventgrid.azure.net/api/events"
   r = requests.post(url, headers=headers, data=data2)
   # print(r.status_code)
   return r


s = '85d89569-5c9e-4fc6-a394-7bb9d724b614'
p = '{"AppName": "SomeApp", "PermName": "SomePermission", "ChangeRequestType": "ADD"}'
k = 'SbBjasdfasdf'
req = send_req(s, p, k)
print(req.status_code)

if req.status_code == 200:
   print("good")
else:
      pass