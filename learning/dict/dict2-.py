# {
#    "id": "file",
#    "value": "File",
#    "popup": {
#       "menuitem": [
#          {"value": "New", "onclick": "CreateNewDoc()"},
#          {"value": "Open", "onclick": "OpenDoc()"},
#          {"value": "Close", "onclick": "CloseDoc()"}
#       ]
#    }
# }

import json
f = open('data.json')
data = json.load(f)
f.close()

for (k, v) in data.items():
   print("Key: " + k)
   print("Value: " + str(v))

# prints:
# Key: id
# Value: file
# Key: value
# Value: File
# Key: popup
# Value: {'menuitem': [{'value': 'New', 'onclick': 'CreateNewDoc()'}, {'value': 'Open', 'onclick': 'OpenDoc()'}, {'value': 'Close', 'onclick': 'CloseDoc()'}]}