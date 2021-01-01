#!/usr/bin/env python3

################################################################
# Text
################################################################

# pg 279
with open('./files/quotes.txt','r') as f:
    for one_line in enumerate(f.readlines()):
        # if counter is even, print with no extra newline
        if one_line[0] %2 == 0:
            print(one_line[1],end='')
        # otherwise print a couple spaces and add an extra newline
        else:
            print('  ' + one_line[1])