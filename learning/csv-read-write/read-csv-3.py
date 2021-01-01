#!/usr/bin/env python3

################################################################
# Same as before, but place in functions, return as dict
################################################################

#pg 301

import datetime as dt
import csv

def fname(any):
    try:
        nm = any.split(",")
        return nm[1]
    except IndexError:
        return ""

def lname(any):
    try:
        nm = any.split(",")
        return nm[0]
    except IndexError:
        return ""

def integer(any):
    return int(any or 0)

def date(any):
    try:
        return dt.datetime.strptime(any, "%m/%d/%Y").date()
    except ValueError:
        return None

def boolean(any):
    return bool(any)


def floatnum(any):
    s_balance = (any.replace("$", "").replace(",", "")).strip()
    return float(s_balance or 0)

# create empty dict
people = {}

with open("C:\\_gwill\\repo-home\\h1python\\learning\\csv-read-write\\sample.csv", encoding="utf-8", newline="") as f:
    # reader = csv.reader(f)
    # optional, print row number
    reader = enumerate(csv.reader(f))

    # skip first row
    f.readline()

    # read through next rows with i as counter
    for i, row in reader:

        # from each row create person object with a unique id
        newdict = dict(
            {
                "first_name": fname(row[0]),
                "last_name": lname(row[0]),
                "birth_year": integer(row[1]),
                "date_joined": date(row[2]),
                "is_active": boolean(row[3]),
                "balance": floatnum(row[4]),
            }
        )
        people[i + 1] = newdict
        
# When loop is done, show all people
for person in people.keys():
    id = person
    print( id, people[person]['first_name'], \
        people[person]['last_name'], \
        people[person]['birth_year'], \
        people[person]['date_joined'], \
        people[person]['is_active'], \
        people[person]['balance'])

