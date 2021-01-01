#!/usr/bin/env python3

################################################################
# Text
################################################################

# hastables/dictionary
# note a comma (,) after each key-value pair
# and colon (:) between the Key-value pair instead of 'equals to' (=) used in PowerShell
table = {} # empty hashtable
table = dict()  # alternative way to create empty hastable

# hashtable with integer keys
table = {
1 : 'one',
2 : 'two',
3 : 'three'
}

# hashtable is a data stucture that has key-value pair as a element
table = {
'firstname' : 'prateek', # in powershell single/double quotes around 'string keys' are optional, but not in python
'lastname' : 'singh'
}

# adding key-value pairs or replace any existing key
age = {}
age['prateek']=27
age['sam']=31
age['susan']=25

# get dictionary keys or values
age.keys()
age.values()

# returns a boolean true/false if key matches
age.__contains__('sam')

# iterating through key-value pairs
for key, value in age.items():
    print("key: {0}, value: {1}".format(key, value))


# created nested dictionary
employee = {
'name': {
    'firstname': 'prateek',
    'lastname': 'singh'
    },
'dateofjoining': {
    'day': 1,
    'month': 5,
    'year': 2017
    }
}

age
{ 'gerry': 31, 'sam': 29, 'billy':10, 'sally': 18}
# Deleting a key-value pair
age.__delitem__('gerry')

# accessing nested dictionary items
print(table['name']['firstname'])
print(table['dateofjoining']['year'])

# >>> age = {}
# >>> age['gerry'] = 31
# >>> age['sam'] = 29
# >>> age['billy']=10
# >>> age['sally']=18
# >>> age
# {'gerry': 31, 'sam': 29, 'billy': 10, 'sally': 18}
# >>> age.__delitem__('gerry')
# >>> age
# {'sam': 29, 'billy': 10, 'sally': 18}
# >>> age.pop('sam') # deletes, the key-value pair but returns the value
# 29
# >>> age
# {'billy': 10, 'sally': 18}
# >>> age.popitem()
# ('sally', 18)
# >>> age
# {'billy': 10}
# >>>


# sorting a dictionary
numbers = {
5 : 'five',
3 : 'three',
1 : 'one',
2 : 'two',
4 : 'four'
}

dict(sorted(numbers.items())) # ascending order
dict(sorted(numbers.items(),reverse=True)) # descending order
