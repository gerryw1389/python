#!/usr/bin/python3

################################################################
# Text
################################################################

#pg 315


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

# now you can loop through collection
for k,v in hits_data.items():
    print( f"{k}. {v['count']:>5} - {v['page']}" )
    
# Using positionals
for k,v in hits_data.items():
    print( '{}. {:>5} - {}'.format(k, v['count'], v['page']))