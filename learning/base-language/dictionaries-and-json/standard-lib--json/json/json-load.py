#!/usr/bin/env python3

################################################################
# Text
################################################################

import json

filename = './hitcounts.json'

with open(filename, 'r', encoding='utf-8', newline='') as f:
    hits = json.load(f)
    
print(type(hits))
# <class 'dict'>

for p in hits:
    print(p)
    # prints 1 and 2 which are the keys
    
for k,v in hits.items():
    print(k,v)
    # prints dictionary
    
    
for k,v in hits.items():
    print(v['count'])
    # prints one part of dictionary - 9071 and 9074
    
for k,v in hits.items():
    if k == "1":
        print(v['count'])
        # prints only 9071 since its key is equal to "1"