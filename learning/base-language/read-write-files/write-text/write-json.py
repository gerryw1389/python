#!/usr/bin/env python3

################################################################
# Similar to write json, this will
# Call greet_user() which will check for a username file
#   If it exists, it greets the user
#   If it doesn't, it creates the file so that it will work on next run
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



def get_stored_username():
    """Get stored username if available."""
    filename = f"{rel_path}files/username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = f"{rel_path}files/username.json"
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()