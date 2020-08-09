#!/usr/bin/python3

################################################################
# Text
################################################################

# First, create myfile.txt with text 'hello world' on one line
# Next, create myfile2.txt with text 'hellow world' on two lines

class Error(Exception):
    ''' Base class for other exceptions'''
    pass

# here we define our own error
class EmptyFileError(Error):
    pass

try:
    thefile = open('./files/myfile2.csv','r')
    # for some reason, when I uncomment these I don't get it to read the lines in the else block but still get success?
    #line_count = len(thefile.readlines())
    #if the file has less than 2 lines, throw our own error
    #if line_count < 2:
    #  raise EmptyFileError
except FileNotFoundError:
    # catch if file doesn't exist
    print("there is no myfile.txt")
except EmptyFileError:
    # catch our custom error
    print('your text file has less than two lines')
except Exception as e:
    # catch any other exception
    print('Failed: Exception was ' + str(e))
    thefile.close()
else:
    # yay! we made it without errors, let's read the file!
    print()
    for one_line in thefile:
        # and end='' in order for there not to be spaces for each line
        #print(one_line,end='')
        print(one_line)
    thefile.close()
    print('Success!')
