# Author: Brandon Hoffman
# Date: 10/29/2020
# Description: Mutates a given list and squares the items in the list

def square_list(lst) -> None:
    """
    Input: a list of numbers
    Doesn't return anything, mutates given list
    """
    i: int
    for i in range(len(lst)):
        lst[i] **= 2


# Testing

numb_lists: list[int] = [1, 2, 3, 4]
square_list(numb_lists)
print(numb_lists)  # This should print [1, 4, 9, 4]
