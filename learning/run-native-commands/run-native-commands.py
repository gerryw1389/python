#!/usr/bin/env python3

################################################################
# Example of subprocess and running native commands in python
# Have not tested extensively
################################################################

import subprocess
from os import system, name

def run_this():
    if name == 'nt': 
        process_name = 'ipconfig'
        print('Running: ', process_name)
        st = subprocess.run(process_name, shell=True, stdout=subprocess.PIPE)
        print(st.stdout)
        print(type(st))
    else: 
        process_name = 'systemctl status firewalld'
        print('Running: ', process_name)
        st = subprocess.run(process_name, shell=True, stdout=subprocess.PIPE)
        print(st)
    return f"completed running: {process_name}"

def run_this_2():
    if name == 'nt': 
        process_name = 'ipconfig'
        print('Running: ', process_name)
        st = subprocess.run([process_name, '/all'], shell=True, check=True)
        print(st)
    else: 
        process_name = 'systemctl status firewalld'
        print('Running: ', process_name)
        st = subprocess.run(process_name, shell=True, stdout=subprocess.PIPE)
        print(st)
    return f"completed running: {process_name}"


command = run_this()
print(command)

command2 = run_this_2()
print(command2)