#!/usr/bin/env python3

################################################################
# Appends text to a file
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
filename = f"{rel_path}files/programming.txt"

with open(filename, 'a') as file_object:
    file_object.write("text1.\n")
    file_object.write("text2.\n")

# this does not work because it will just create the file!
# try:
#     with open(filename, 'a') as file_object:
#         file_object.write("text1.\n")
#         file_object.write("text2.\n")
# except FileNotFoundError:
#     print(f"File does not exist: {filename}")
