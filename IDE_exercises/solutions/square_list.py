# Author: Brandon Hoffman
# Date: 10/29/2020
# Description: Mutates a given list and squares the items in the list

def square_list(lst):
    """
    Input: a list of numbers
    Doesn't return anything, mutates given list
    """

    for i in range(len(lst)-1):
        lst[i] **= 2
