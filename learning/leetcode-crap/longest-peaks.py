# Peaks

'''
Returns the longest peak based on an input list. 
Can return a list object but will return just the length of longest peak by default.
A peak is defined as adjacent integers in the array that are increasing until it reaches a tip.
The tip is the highest value in the peak. What comes after the peak should be decreasing integers.
At least 3 integers are required to form a peak.
Examples:
[1, 4, 10, 2] # forms a peak because all requirements are met.
[4, 0, 10] # does not form a peak because there is no rise in numbers.
[1, 2, 3] # is not a peak because there aren't any decreasing integers after the 3.

Inputs: List object - https://docs.python.org/3/tutorial/datastructures.html?highlight=lists
Outputs: Int object - https://docs.python.org/3.6/library/stdtypes.html?highlight=int
'''

def findLongestPeak(my_list):
    
    # Check if it's a list with all ints
    if type(my_list) != list:
        return None
    else:
        for m in my_list:
            if type(m) == int:
                pass
            else:
                return None
    
    # peaks detection = https://stackoverflow.com/questions/53914486/detect-peaks-in-list-of-numbers-and-record-their-positions#53914719
    def peaks(ar):
        i, up = 0, False
        for r in range(1, len(ar)):
            prev, val = ar[r-1], ar[r]
            if up and val < prev:
                yield prev, i
                up = False
            if val > prev:
                i, up = r, True

    try:
        peaks_generator = peaks(my_list)
        peaks_list = (list(peaks_generator))
    except:
        return None

    #print(f"Peaks lists: {peaks_list}")

    master_list = []
    back_list = []
    forward_list = []
    
    for peak in peaks_list:
        max_num_index = peak[1]
        #print(f"Processing index: {max_num_index} which is value {my_list[max_num_index]}")

        
        # First, make sure it is not first or last index
        if (max_num_index + 1) != len(my_list) or max_num_index != 0 :
                
                # If the next index value is less than current max, continue
                if my_list[max_num_index + 1] < my_list[max_num_index]:
                    
                    # if the previous index is less than current max, continue
                    if my_list[max_num_index - 1] < my_list[max_num_index]:
                        
                        # Loop backwards and add all values that are less than the max
                        for r in range( (max_num_index - 1), -1, -1):
                            if r == (max_num_index - 1):
                                if my_list[r] < my_list[max_num_index]:
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
                            if r == (max_num_index + 1):
                                if my_list[r] < my_list[max_num_index]:
                                    forward_list.append(my_list[r])
                                else:
                                    return None
                            else:
                                if my_list[r] < forward_list[-1]:
                                        forward_list.append(my_list[r])
                                else:
                                    break
                        
                        # collect the results and clear lists for next iteration
                        joined_list = back_list[::-1]
                        joined_list.append(my_list[max_num_index])
                        for f in forward_list:
                            joined_list.append(f)
                        master_list.append(joined_list)
                        back_list.clear()
                        forward_list.clear()
                    else:
                        return None # prior value was not less than peak
                else:
                    return None # next value was not less than peak
        else:
            return None # peak was either first or last element in list

    #print(f"Master lists: {master_list}")
    if len(master_list) == 1:
        #return master_list[0]
        return len(master_list[0])
    else:
        try:
            return_list = max(master_list, key=len)
            #return return_list
            return len(return_list)
        except ValueError:
            return None 



# Pass:
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3] # Returns 6 for [0, 10, 6, 5, -1, -3]
#array = [1, 2, 3, 3, 4, 0, 10, 6, 5, 4, 1, -1, -3, -3, -3, 2, 3] # Returns 8 for [0, 10, 6, 5, 4, 1, -1, -3]
#array = [1, 4, 10, 2] # Returns 4 for [1, 4, 10, 2].
#array = [1, 40, 10, 2, 40, 3, 2, 1] # Returns 5 for [2, 40, 3, 2, 1]. Forms two peaks with same highest value and returns the longer appropriately.
#array = [1, 30, 10, 2, 20, 3, 2, 1] # Returns 5 for [2, 20, 3, 2, 1]. forms two peaks, but since second is longer, returns appropriately.
#array = [5, 6, 8, 3, 4, 5, 5, 5, 10, 2, 1, -1, -3, -5] # Returns 7 for [5, 10, 2, 1, -1, -3, -5]

# Fail:
#array = [10, 1, 2, 3] # highest number is first
#array = "bob" # is not a list
#array = [1, 2, "bob", 3, 4, 0, 10, 6, 5, -1, -3, 2, 3] # has a string
#array = [4, 0, 10] # does not form a peak because there is no rise in numbers.
#array = [1, 2, 3] # is not a peak because there aren't any decreasing integers after the 3.

longest_peak_response = findLongestPeak(array)
print(longest_peak_response)
