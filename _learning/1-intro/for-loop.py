#!/usr/bin/python3

################################################################
# Text
################################################################

# For loops are often used to iterate through collection objects:

# Iterate through lists
shuttles = ['columbia', 'endeavour', 'challenger','discovery', 'atlantis', 'enterprise', 'pathfinder']

# Read shuttles list and enumerate into index and value
for index, value in enumerate(shuttles):
    print(index, value)

'''
prints:
0 columbia
1 endeavour
2 challenger
3 discovery
4 atlantis
5 enterprise
6 pathfinde
'''

# Iterate through lists 2: using the enumerate() function to get index instead 
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for i,d in enumerate(days):
    print(i,d)


# Iterate through dictionary
dnsservers = {}
dnsservers = {"us": "ns1.cyberciti.com", "uk": "ns2.cyberciti.biz", "asia": "ns3.cyberciti.org"  }

# Python for loop for key,value using dict data type
# for key, value in dict.items():
for location, server in dnsservers.items():
    print(server, "dns server is located in", location)

'''
returns:
ns1.cyberciti.com dns server is located in us
ns2.cyberciti.biz dns server is located in uk
ns3.cyberciti.org dns server is located in asia
'''

# basic for loop
# Prints out 1,2,3,4
for i in range(1, 10):
    if( i %5 == 0 ):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

# use the break and continue statements
print('*'*10)
custom_range = range(5,30)
for x in custom_range:
    #if (x == 7): 
    #    break  # when x ==7 loop will end and next block of code will execute 
    if (x %2 == 0) : 
        continue # when x == even number, loop will go back to start and run again ignoring the even numbers and only printing odd numbers
    print(x)