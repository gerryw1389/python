#!/usr/bin/env python3

################################################################
# Text
################################################################

import json

hits = {
    '1': {
        'data1' : 'data'
    },
    '2': {
        'data1' : 'data'
    }
}
with open('hitcounts_new.json', 'w', encoding='utf-8') as out_file:
    json.dump(hits, out_file, ensure_ascii=False, sort_keys=True)