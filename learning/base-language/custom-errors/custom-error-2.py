#!/usr/bin/env python3

################################################################
# Check for 'myfile.csv' in a certain directory
# Since this has more than two lines, it will output the files contents

# You should also try renaming to 'myfile3.csv' and re-running to ensure it catches it
################################################################

class Error(Exception):
    ''' Base class for other exceptions'''
    pass

# here we define our own error
class EmptyFileError(Error):
    pass

try:
    filename = 'C:\\_gwill\\repo-home\\h1python\\learning\\base-language\\custom-errors\\myfile2.csv'
    
    #Use `with open(filename, encoding='utf-8') as thefile:` if the file has special chars
    with open(filename) as thefile:

        #if the file has less than 2 lines, throw our own error
        file_content = thefile.readlines()

        # At this point, file_content should contain a list like ['FirstName,LastName\n', 'Darth,Vader']
        line_count = len(file_content)
        if line_count < 2:
            raise EmptyFileError
except FileNotFoundError:
    # catch if file doesn't exist
    print("there is no myfile2.csv")
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
    
    # since we did readlines(), it is a list object so we loop through and print
    # If we instead did read() then you would just print
    for one_line in file_content:
        # and end='' in order for there not to be line breaks for each line
        #print(one_line)
        print(one_line, end='')
    thefile.close()
    
    #print('Success!')
