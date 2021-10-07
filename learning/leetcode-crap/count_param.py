
# https://pythonprinciples.com/challenges/Counting-parameters/

'''
Counting parameters

Define a function param_count that takes a variable number of parameters. The function should return the number of arguments it was called with.

For example, param_count() should return 0, while param_count(2, 3, 4) should return 3.

'''

def param_count(*args):
    return(len(args))

param_count()
param_count(2, 3, 4)

'''
def param_count(*args):
    return len(args)
'''