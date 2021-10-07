# Largest Peaks

'''
Returns the largest peak based on an input list.
A peak is defined as adjacent integers in the array that are increasing until it reaches a tip.
The tip is the highest value in the peak. What comes after the peak should be decreasing integers.
At least 3 integers are required to form a peak.
Examples:
[1, 4, 10, 2] # forms a peak because all requirements are met.
[4, 0, 10] # does not form a peak because there is no rise in numbers.
[1, 2, 3] # is not a peak because there aren't any decreasing integers after the 3.

Inputs: List object - https://docs.python.org/3/tutorial/datastructures.html?highlight=lists
Outputs: List object - https://docs.python.org/3/tutorial/datastructures.html?highlight=lists
'''

def findlargestPeak(my_list):
    
    # Check if it's a list with all ints
    if type(my_list) != list:
        return None
    else:
        for m in my_list:
            if type(m) == int:
                pass
            else:
                return None

    # Get max and make sure it's past index 1
    max_num = max(my_list)
    max_num_index = my_list.index(max_num)
    if max_num_index >= 1:
        pass
    else:
        return None
    
    back_list = []
    forward_list = []

    # First, make sure it is not last index
    if (max_num_index + 1) != len(my_list):
            
            # If the next index value is less than max, continue
            if my_list[max_num_index + 1] < max_num:
                
                if my_list[max_num_index] > my_list[max_num_index - 1]:
                    pass
                else:
                    return None
                
                # Loop backwards and add all values that are less than the max
                for r in range( (max_num_index - 1), -1, -1):
                    if my_list[r] == my_list[max_num_index - 1]:
                        if my_list[r] < max_num:
                            back_list.append(my_list[r])
                        else:
                            return None
                    else:
                        if my_list[r] < back_list[-1]:
                            back_list.append(my_list[r])
                        else:
                            break
                # Now Loop forwards and add all values that are less than the max
                for r in range( (max_num_index + 1), len(my_list)):
                    if my_list[r] == my_list[max_num_index + 1]:
                        if my_list[r] < max_num:
                            forward_list.append(my_list[r])
                        else:
                            return None
                    else:
                        if my_list[r] < forward_list[-1]:
                                forward_list.append(my_list[r])
                        else:
                            break
                # Send back a response
                joined_list = back_list[::-1]
                joined_list.append(max_num)
                for f in forward_list:
                    joined_list.append(f)
                return joined_list
            else:
                return None
    else:
        return None

# Pass:
#array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3] # [0, 10, 6, 5, -1, -3]
#array = [1, 4, 10, 2] # [1, 4, 10, 2]
#array = [1, 40, 10, 2] # [1, 40, 10, 2]
#array = [1, 40, 10, 2, 40, 3, 2, 1] # # [1, 40, 10, 2] Two peaks equal value only returns first one.
#array = [1, 2, 3, 4, 5, 6, 7, 40, 10, 2, 50, 3, 2, 1] # [2, 50, 3, 2, 1] Grabs second peak because it is higher

# Fail:
#array = [10, 1, 2, 3] # None because highest number is first element in list (no decreasing numbers before)
#array = "bob" # None because is not a list
#array = [1, 2, "bob", 3, 4, 0, 10, 6, 5, -1, -3, 2, 3] # None because list has a string
#array = [4, 0, 10] # None because no peak is formed
#array = [1, 2, 3] # None because peak is last element in list (no decreasing numbers after)

largest_peak_response = findlargestPeak(array)
print(largest_peak_response)
