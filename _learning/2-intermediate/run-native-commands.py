#!/usr/bin/python3

################################################################
# Example of subprocess and running native commands in python
################################################################

import subprocess

stat = 'systemctl status firewalld'
print('Running: ', stat)
st = subprocess.run(stat, shell=True, stdout=subprocess.PIPE)
print(st)