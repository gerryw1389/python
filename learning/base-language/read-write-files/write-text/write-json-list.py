#!/usr/bin/env python3

################################################################
# Exports a text file in json format to be imported as a list
################################################################

import json
import sys
import os

# get script path from arguments
path = str(sys.argv[0])
path_list = list(path.split("/"))

# build a relative path excluding the last argument
rel_path = ''
for path in path_list[0:-1]:
    rel_path = rel_path + path + os.sep

# Use that as the basis for importing the file
filename = f"{rel_path}files/numbers.json"

numbers = [2, 3, 5, 7, 11, 13]

with open(filename, 'w') as f:
    json.dump(numbers, f)
