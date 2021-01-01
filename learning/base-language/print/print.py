#!/usr/bin/env python3

################################################################
# Different ways to use print
################################################################

# Example 0: For python 3.6+, use f-strings most often
name = 'Gerry'
adjective = 'funny'
noun = 'person'
verb = 'runs'
print(f"Example 0: {name} is a {adjective} {noun} that {verb}")

# Example 1: Cast var to string (if not already)
print("Example 1: This is a string " + str(123) )

# Example 2: multiple vars
name = 'Gerry'
adjective = 'funny'
noun = 'person'
verb = 'runs'
print('Example 2:',name,'is a',adjective,noun,'that',verb)
# notice the commas will add spaces, not really sure why?

# Example 3: Positional
# This is my go-to if I'm not doing f strings
string = 'Example 3: {} is a {} {} that {}'.format(name, adjective,noun,verb)
print(string)
# Gerry is a funny person that runs

# Example 4: Use numbers in braces to define sequence of arguments consumed by the string
string = 'Example 4: a:{0} b:{2} c:{1}'.format('red','green','blue')
print(string)
# 'a:red b:blue c:green'

# Example 5: Adding zeros
string = 'Example 5: {0:03d}'.format(5)
print(string)
#'005'

# Example 6: Using dictionaries for formatting
coor = {'latitude': '31.24E', 'longitude': '-125.181N'}
string = 'Example 6: Coordinates: {latitude}, {longitude}'.format(**coor)
print(string)
# 'Coordinates: 31.24E, -125.181N'