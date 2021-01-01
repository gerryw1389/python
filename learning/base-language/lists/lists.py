#!/usr/bin/env python3

################################################################
# lists
################################################################

days = ["Mon","Tue","Wed","Thu","Fri","Sat"]
print(days)  # this will print arrays in array format

#printing all elements of an array
for d in days: 
    print(d)


# creating empty lists
fruits = []
fruits = list()

# adding elements to list
fruits.append('apple')
fruits.append('banana')
fruits.append('orange')


# >>> cars.append("ford")  
# >>> print(cars)
# ['ford']
# >>> cars.append("chevy") 
# >>> print(cars)
# ['ford', 'chevy']
# >>> print(cars[0]) 
# ford
# >>> print(cars[1]) 
# chevy
# >>>print(len(cars))
# 2


# change value
## >>> cars[-1] = 'kia'
## >>> print(cars)
##['ford', 'kia']
##>>>

# insert at element number:
#vowel.insert(3, 'u')  # .insert(index, element)

# to reverse a list
# >>> array = list('spongebob') 
# >>> reversed(array) # doesn't work
# <list_reverseiterator object at 0x035D2790>
# >>> list(reversed(array))
# ['b', 'o', 'b', 'e', 'g', 'n', 'o', 'p', 's']
# >>>



# assigning list elements to multiple variables
array = [1,2,3,4,5]
a,b,c,d,e = array
# this will assign a the value of 1, b the value of 2 and so on...

# example
# >>> array = [2,4,6,18]
# >>> gerry, bob, tim, jim = array
# >>> gerry
# 2   
# >>> time
# Traceback (most recent call last):   
# File "<stdin>", line 1, in <module>
# NameError: name 'time' is not defined
# >>> time
# Traceback (most recent call last):   
# File "<stdin>", line 1, in <module>
# NameError: name 'time' is not defined
# >>> tim
# 6   


# delete elements of an array using del, remove() and pop()
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
# deleting by index
del colors[4]
# deleting by value
colors.remove("blue") # removes only the first occurrence
colors.pop(3) # .pop(index) deletes and returns the element
print(colors)

# slicing lists
# array[startindex:end:step]
animal = ["dog", "cat", "cow", "pig", "giraffe"]
print(animal[1:4]) # animal[start:end] items start through end-1
print(animal[-3:-1])
print(animal[2:]) # animal[start:] items start through the rest of the array
print(animal[-4:])
print(animal[:3]) # animal[:end] items from the beginning through end-1
print(animal[:]) # copy of the whole array
print(animal[1:4:2]) # animal[start:end:step]  start through not past end, by step

# two dimensional lists

# creating 2D lists
array = [1, 2, [3.1, 3.2, 3.3], 4]
array[2][1] # fetching values
array[2][2]
array[2][0] = 5 # assigning values
print(array)

# tuples cannot be modified, read only  - no add, delete
tuple = (5, 6, 7, 18) # () parenthesis to create tuples
print('Tuple:', tuple)
print("Tuple index 1:", tuple[1])  # number in square bracket is index of element you want to access

# define sets
x = set('python')
y = set('powershell')

print(x - y) # All the elements in x but not in y
# union
print(x | y) # Unique elements in x or y or both
# intersection
print(x & y) # Elements in both x and y
print(x ^ y) # Elements in x or y but not in both


###################################
## Arrays ##
###################################
# import the module, since Array is not a native data structure

import array
a = array.array("I",[1,2,3,4,5]) # homogeneous, strong typed array
type(a) # get data type of the array
# not implicitly typecasted, you've to explicitly typecast elements with the array data type
a = array.array("I",[1,2,3,int(4.3),5]) 
# throws error 'TypeError: integer argument expected, got float'
a = array.array("I",[1,2,3,4.3,5]) 

# operations on array
a.insert(1,7) # inserting elements
a.pop(3) # delete and return an element
a.reverse() # reverse the array

# access elements
a[0] # list first element
a[-1] # list last element

import array as arr

numbers_list = [2, 5, 62, 5, 42, 52, 418, 5]
numbers_array = arr.array('i', numbers_list)

print(numbers_array[2:5]) # 3rd to 5th
print(numbers_array[:-5]) # beginning to 4th
print(numbers_array[5:])  # 6th to end
print(numbers_array[:])   # beginning to end

# see https://www.programiz.com/python-programming/array
# Unless you don't really need arrays (array module may be needed to interface with C code), their use is not highly recommended.


cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# Tuple
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

even_numbers = list(range(2, 11, 2)) 
print(even_numbers)


## copy lists

my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

## list comprehension

squares = [value**2 for value in range(1, 11)]
print(squares)

## not in list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
	
	
## in keyword

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
		
