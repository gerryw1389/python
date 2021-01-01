#!/usr/bin/env python3

################################################################
# Example reading a file and counting its words
# not sure if this is the best way, but it was fun and it worked!
################################################################

import os

script_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_path)

filename = "files/alice.txt"

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
