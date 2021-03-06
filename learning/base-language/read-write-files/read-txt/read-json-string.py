#!/usr/bin/env python3

################################################################
# Imports a text file that was exported in json format
# Result is a string object
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
filename = f"{rel_path}files/username.json"

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
