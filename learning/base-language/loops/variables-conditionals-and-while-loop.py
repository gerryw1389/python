#!/usr/bin/env python3

################################################################
# In WSL, first time setup:
# sudo apt-get update && sudo apt-get upgrade -y && sudo apt clean && sudo apt autoremove
# sudo apt-get install python3-pip

# Don't spend too much time here, just see my post at https://automationadmin.com/2020/06/python-basic-syntax
################################################################

###################################
## Variables ## 
###################################

# assign var
a = 5
print(a)

# one to many
a = b = c = 3
print(a)
print(b)
print(c)

# many to many
a, b, c = 1, 4, 'gerry'
print(a)
print(b)
print(c)

# read input
name = input("Enter your name: ")
print(name)

###################################
## Conditionals ## 
###################################
# python doesn't have switch cases, I pretty much just use if, elif, else instead
print("\n\nConditional:")
x, y = 100, 100

# conditional flow uses if, elif, else  
if(x < y):
    st = "x is less than y"
elif(x == y):
    st = "x is the same as y"
else:
    st ="x is greater than y"

print(st)
# x is the same as y

###################################
## While Loop ##
###################################

# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

# Same thing, breaks on 5 or else would be infinite loop
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

count=0
while(count<5):
    print(count)
    count +=1
else:
    # print("count value reached %d" %(count)) # older string formatting https://python-reference.readthedocs.io/en/latest/docs/str/formatting.html
    print('count reached {}'.format(count))

###################################
## Inspections ##
###################################

f = 0
type(f)
# tells you the class. You can then look it up in python docs
# or directly in the terminal:
help(f)

