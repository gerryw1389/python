# https://pythonprinciples.com/challenges/Middle-letter/

'''
Middle letter

Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
'''

def mid(str):
    if len(str) % 2 == 0:
        #print("string has even")
        return ""
    else:
        #print("string has odd")
        return str[(len(str)-1)//2:(len(str)+2)//2]

s = "abc"
middle_letter = mid(s)
print(middle_letter)

'''
# this approach uses // which is integer division in Python 3
# alternatively, use / and int() in combination.
def mid(string):
    if len(string) % 2 == 0:
        return ""
    return string[len(string)//2]
'''