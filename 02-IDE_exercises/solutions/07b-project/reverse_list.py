# Author: Luis Mercado
# Date: 10/24/2024
# Description: Function that mutates a list of numbers by reversing its order without slicing


def reverse_list(num_list: list[int | float]) -> None:
    """
    Mutates list of numbers (float or int) into reverse order
    without using any slicing (no return value)
    """
    
    # Define lower limit of desired index range which is the same as upper limit of starting list argument
    low_lim: int = len(num_list)-1
    
    # For range must use negative stride and go to -1 so that 0 index is included
    for num in range(low_lim, -1, -1):
        num_list.append(num_list[num]) # Adds currently indexed list value to end of list
        del num_list[num] # Deletes original iteration of currently indexed value from list

    # No return value, but by using .append and del[], the original num_list argument has iteratively had its last
    # value duplicated to the end and then had the original occurrence of it deleted so that the list is now
    # effectively in the opposite order