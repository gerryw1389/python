#!/usr/bin/env python3

################################################################
# Example reading a file and counting its words
# not sure if this is the best way, but it was fun and it worked!
################################################################

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
filename = f"{rel_path}files/alice.txt"

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
