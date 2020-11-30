#!/usr/bin/python3

################################################################
# Script Arguments
# sys.argv is list of arguments passed to the script
# sys.argv[0] is by default the path of script
# and user defined arguments start with index 1
################################################################

import sys

# Print total number of arguments
print('Total number of arguments:', format(len(sys.argv)))

# Print all arguments
print('Argument List:', str(sys.argv))

# Print arguments one by one
print('First argument:',  str(sys.argv[0]))
print('Second argument:',  str(sys.argv[1]))
print('Third argument:',  str(sys.argv[2]))

bob = str(sys.argv[0])
print("magically, the filename for this script is: " + bob)
# save and exit
# now type `chmod +x ./max.py` and `python3 ./max.py 13 23 57`
