#!/usr/bin/python3

################################################################
# Text
################################################################

print("This is a string " + str(123) )

# multiple vars
name = 'Gerry'
adjective = 'funny'
noun = 'person'
verb = 'runs'
print(name,'is a',adjective,noun,'that',verb)

# positional
print('{} is a {} {} that {}'.format(name, adjective,noun,verb))
# Gerry is a funny person that runs

# use numbers in braces to define sequence of arguments consumed by the string
'a:{0} b:{2} c:{1}'.format('red','green','blue')
# 'a:red b:blue c:green'

# adding zeros
'{0:03d}'.format(5)
#'005'

# using dictionaries for formatting
coor = {'latitude': '31.24E', 'longitude': '-125.181N'}
'Coordinates: {latitude}, {longitude}'.format(**coor)
# 'Coordinates: 31.24E, -125.181N'