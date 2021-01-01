#!/usr/bin/env python3

################################################################
# Text
################################################################

class Error(Exception):
    ''' Base class for other exceptions'''
    pass

# here we define our own error
class EmptyFileError(Error):
    pass

try:
    thefile = open('./z_py/myfile2.txt')
    #line_count = len(thefile.readlines())
except Exception as e:
    print(e)
else:
    #lines = thefile.readlines()
    for one_line in thefile:
        print(one_line)
    thefile.close()
    print('Success!')