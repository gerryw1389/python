#!/usr/bin/env python3

################################################################
# Text
################################################################


try:
    file = open("./z_py/myfile2.txt")
    print(file.name)
except Exception as e:
    print("file not found")
    print(e)
else:
    print("\n")
    print(file.readline())
    file.close()
    print("success")
finally:
    print("this will run no matter what")

try:
    file = open("./z_py/myfile2.txt")
    print(file.name)
except Exception as e:
    print("file not found")
    print(e)
else:
    print("\n")
    print(file.readline())
    file.close()
    print("success")
finally:
    print("this will run no matter what")
