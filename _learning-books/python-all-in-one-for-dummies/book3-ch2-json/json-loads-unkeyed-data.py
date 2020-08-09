#!/usr/bin/python3

################################################################
# Text
################################################################

#pg 314

import json

json_string = '''
    {
   "website": [
      {
         "count": 9071,
         "lastreferrer": "https://something.com",
         "page": "/downloads.html"
      },
      {
         "count": 9074,
         "lastreferrer": "https://somethingelse.com",
         "page": "/downloads2.html"
      }
   ]
}
'''

# Load json from string
website_data = json.loads(json_string)

# now you can loop through collection
for w in website_data['website']:
    print(w['count'], w['page'])
    
# Using my preferred method
for w in website_data['website']:
    print('{} {}'.format(w['count'], w['page']))