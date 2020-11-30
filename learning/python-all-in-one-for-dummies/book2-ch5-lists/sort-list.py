#!/usr/bin/python3

################################################################
# From an imported list, this will sort and return a string
# pg 202
################################################################

def alphalist( orginal_list=[] ):
    
    # Create working copy of list passed in
    sorted_list = orginal_list.copy()
    
    sorted_list.sort()
    
    final_list = ''
    
    for name in sorted_list:
        final_list += name + ', '
    
    # strip the ending comma and space
    final_list = final_list[:-2]
    
    # To return a list instead of a string, uncomment these lines and comment out the original return statement
    # new_list = []
    # splitOrig = final_list.split(', ')
    # for item in splitOrig:
    #     new_list.append(item)
    # return new_list
    
    return final_list

# Call function
list = [ 'a', 'q', 'b']
new_list = alphalist(list)

print(new_list)

print('new list type = ')
print(type(new_list))

# preferred, single line
print('new list type = ',end='')
print(type(new_list))
