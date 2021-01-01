#!/usr/bin/env python3

################################################################
# Imports a text file
# Prints its output. 
#   If the index of the line is even, don't include a line break
#   If the index of the line is odd, include a line break and spaces at begining
################################################################

import sys
import os

# get script path from arguments
path = str(sys.argv[0])
path_list = list(path.split("/"))

# build a relative path excluding the last argument
rel_path = ''
for path in path_list[0:-1]:
    rel_path = rel_path + path + os.sep

# Use that as the basis for importing the file
filename = f"{rel_path}files/quotes.txt"

with open(filename,'r') as f:
    
    for one_line in enumerate(f.readlines()):
        
        # print(one_line)
        # output: (0, '"The greatest glory in living lies not in never falling, but in rising every time we fall."\n')
        
        # if counter is even, print with no extra newline - remember indexes start at 0 so take line number minus 1!
        
        if one_line[0] %2 == 0:
            # Pay attention that our conditional is comparing one+line[0] which is an index
            # But then printing one_line[1] which is the quote
            print(one_line[1],end='')
        # otherwise print a couple spaces and add an extra newline
        else:
            print('  ' + one_line[1])

# prints:
# "The greatest glory in living lies not in never falling, but in rising every time we fall."
#   Nelson Mandela

# "The way to get started is to quit talking and begin doing."
#   Walt Disney

# "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma â€“ which is living with the results of other people's thinking."
#   Steve Jobs

# "If life were predictable it would cease to be life, and be without flavor."
#   Eleanor Roosevelt

# "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough."
#   Oprah Winfrey

# "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success."
#   James Cameron

# "Life is what happens when you're busy making other plans."
#   John Lennon