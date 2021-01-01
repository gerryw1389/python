#!/usr/bin/env python3

################################################################
# Importing submodules - not my preferred way
################################################################

from os import system, name 
from time import sleep

def clear(): 
    
    if name == 'nt': 
        clear = system('cls') 
    else: 
        clear = system('clear') 
    return clear

# print out some text 
print('hello gerry\n'*10) 

# sleep for 2 seconds after printing output 
sleep(2) 

# now call function we defined above 
clear()