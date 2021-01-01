#!/usr/bin/env python3

################################################################
# This time we import then entire modules instead of submodules
# This is my preferred way for standard library modules (heavily tested),
# not third party modules though.
################################################################

import os
import time 

def clear(): 
    # for windows 
    if os.name == 'nt': 
        clear = os.system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        clear = os.system('clear') 
    return clear

# print out some text 
print('hello gerry\n'*10) 

# sleep for 2 seconds after printing output 
time.sleep(2) 

# now call function we defined above 
clear()