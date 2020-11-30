#!/usr/bin/python3

################################################################
# Text
################################################################

#pg 294

import csv
import datetime as dt
from re import sub
with open('sample.csv', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    # optional, print row number
    reader = enumerate(csv.reader(f))
    
    # loop through one row at a time, i is counter, row is entire row
    for i, row in reader:
        
        # ignore header row
        if i > 0:
            try:
                full_name = row[0].split(',')
                last_name = full_name[0].strip()
                first_name = full_name[1].strip()
            except IndexError:
                full_name = first_name = last_name = ''
                
            # birth year is int or 0 for empty string
            birth_year = int(row[1] or 0)
            
            try:
                date_joined = dt.datetime.strptime(row[2], "%m/%d/%y").date()
            except ValueError:
                date_joined = None
            
            # cast to bool
            is_active = bool(row[3])
            
            # remove $, commas, and leading/trailing spaces
            #str_balance = (row[4].replace('$','').replace(',','')).strip()
            
            # If you prefer to use regex:
            str_balance = (sub(r'[\s\$,]','',row[4])).strip()
            
            #balance is a float or 0 for empty string
            balance = float(str_balance or 0)
            
            print(first_name, last_name, birth_year,date_joined,is_active,balance)
print('done')

'''
prints:
Annie Angst 1982 None True 300.0
Marshall Bob 2000 None True 60.0
  0 None False 0.0
Mindy Malaise 2006 None True 550.0
done
'''