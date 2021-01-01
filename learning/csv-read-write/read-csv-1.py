#!/usr/bin/env python3

################################################################
# Import CSV, print index and content for each row
################################################################

import csv

with open('C:\\_gwill\\repo-home\\h1python\\learning\\csv-read-write\\sample.csv', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    # optional, print row number
    reader = enumerate(csv.reader(f))
    
    # loop through one row at a time, i is counter, row is entire row
    for i, row in reader:
        print(i, row)
        
'''
prints:
0 ['Full Name', 'Birth Year', 'Date Joined', 'Is Active', 'Balance']
1 ['Angst, Annie', '1982', '1/11/2011', 'TRUE', '$300.00']
2 ['Bob, Marshall', '2000', '12/10/2001', 'FALSE', '$60.00']
3 ['', '', '', '', '']
4 ['Malaise, Mindy', '2006', '5/5/2005', 'TRUE', '$550.00 ']
'''
