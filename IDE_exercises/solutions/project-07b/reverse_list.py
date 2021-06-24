# Author: Brandon Hoffman
# Date: 10/29/2020
# Description: Mutates a given list and by the order of the elements of teh list

def reverse_list(lst):
    """
    Input: list
    Takes in a list and reverses the order of the elements of the list
    """
    temp_lst = []
    for i in range(len(lst)-1,-1, -1):
        temp_lst.append(lst[i])
    
    lst[:] = temp_lst