#!/usr/bin/env python3

################################################################
# Text
################################################################

# common string operators
string = 'Gerry'

# concatenation
string +' LastName'
#'Gerry LastName'

# repetition
string*5
#'GerryGerryGerryGerryGerry'

# access character at index
string[1]
#'e'

# length of string
len('python')

# find characters at an index
'python'.index('o')

# changing the case
print('hello world'.capitalize())  # capitalize 1st char of the string
print('hello world'.title())  # all words to title case

# splitting a string .split()
print(string.split(' '))  # splitting the string by white space
print(string.split('my'))  # splitting the string by a word, eq. 'my'
print(string.split('\n'))  # splitting by newline character

# joining string .join()
print(' '.join('Gerry'))  # Joining each char with a space
print('*'.join('Gerry'))  # Joining each char with a '*'

# reversing a string reversed()
print(''.join(reversed('python')))  # reversing a string
print(''.join(list('python')[::-1]))  # reversing a string / print(‘Python'[::-1]) is much more elegant and easy to remember

# strip/trim a string .strip() , .lstrip() , .rstrip()
print('   Hey there      '.strip())  # stripping white spaces from both ends of the string
print('   Hey there      '.lstrip())  # stripping white spaces from left end of the string
print('   Hey there      '.rstrip())  # stripping white spaces from right end of the string

# string padding .rjust() .ljust(), .center()
print('Hello'.rjust(30))
print('Hello'.ljust(30, '-'))
print('Hello'.rjust(30, '*'))
print('Hello'.center(30, '_'))


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

name = "Ada Lovelace"
print(name.upper())
print(name.lower())