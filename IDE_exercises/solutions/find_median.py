# Author: Brandon Hoffman
# Date: 10/25/2020
# Description: Sorts a list of numbers and returns the median number in the list

def find_median(some_nums):
    """
    Sorts a list of numbers and returns the median value
    """
    some_nums.sort()
    array_length = len(some_nums)

    mid_index = int(array_length/2)

    if array_length % 2 == 0:
        mid_index_alt = int((array_length/2)-1)
        return (some_nums[mid_index] + some_nums[mid_index_alt]) / 2
    else:
        return some_nums[mid_index]
    