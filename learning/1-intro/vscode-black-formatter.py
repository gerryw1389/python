#!/usr/bin/python3

################################################################
# Using the vscode 'black' formatter for python files
# https://www.geeksforgeeks.org/python-code-formatting-using-black/
################################################################

'''
Before:
def function(name, default=None, *args, variable="1123", a, b, c, employee, office, d, e, f, **kwargs): 
    """This is function is created to demonstrate black"""
  
  
string = 'GeeksforGeeks'
  
j = [1, 
 2, 
 3] 

'''


def function(
    name,
    default=None,
    *args,
    variable="1123",
    a,
    b,
    c,
    employee,
    office,
    d,
    e,
    f,
    **kwargs
):
    """This is function is created to demonstrate black"""


string = "GeeksforGeeks"

j = [1, 2, 3]


'''


Before:
def is_unique( 
               s 
               ): 
    s = list(s 
                ) 
    s.sort() 
  
  
    for i in range(len(s) - 1): 
        if s[i] == s[i + 1]: 
            return 0
    else: 
        return 1
  
  
if __name__ == "__main__": 
    print( 
          is_unique(input()) 
         ) 


'''




def is_unique(s):
    s = list(s)
    s.sort()

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return 0
    else:
        return 1

if __name__ == "__main__":
    print(is_unique(input()))