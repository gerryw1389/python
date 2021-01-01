#!/usr/bin/env python3

################################################################
# Check for 'myfile.csv' in a certain directory
# Since this has less than two lines, it will output as such and exit
################################################################

class Error(Exception):
    ''' Base class for other exceptions'''
    pass

# here we define our own error
class EmptyFileError(Error):
    pass

try:
    filename = 'C:\\_gwill\\repo-home\\h1python\\learning\\base-language\\custom-errors\\myfile.csv'
    
    #with open(filename, encoding='utf-8') as thefile:
    with open(filename) as thefile:

        #if the file has less than 2 lines, throw our own error
        line_count = len(thefile.readlines())
        if line_count < 2:
            raise EmptyFileError
except FileNotFoundError:
    # catch if file doesn't exist
    print("there is no myfile.csv")
except EmptyFileError:
    # catch our custom error
    print('your file has less than two lines, exiting...')
    thefile.close()
except Exception as e:
    # catch any other exception
    print('Failed: Exception was ' + str(e))
    thefile.close()
else:
    # yay! we made it without errors, let's read the file!
    for one_line in thefile.readlines():
        # and end='' in order for there not to be spaces for each line
        #print(one_line,end='')
        print(one_line,end='')
    thefile.close()
    
    print('Success!')
