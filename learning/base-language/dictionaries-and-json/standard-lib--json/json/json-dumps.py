#!/usr/bin/env python3

################################################################
# Text
################################################################

import json

json_string = '''
    {
   "1": {
      "count": 9071,
      "lastreferrer": "https://something.com",
      "page": "/downloads.html"
   },
   "2": {
      "count": 9074,
      "lastreferrer": "https://somethingelse.com",
      "page": "/downloads2.html"
   }
}
'''

# Load json from string
hits_data = json.loads(json_string)

new_dict = json.dumps(hits_data, indent=2)

print(new_dict)