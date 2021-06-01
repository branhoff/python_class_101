# Author: Brandon Hoffman
# Date: 10/04/2020
# Description: Take in number of integers to record from user. Return min and max
#              integers from user

print("How many numbers would you like to enter?")
num_int = int(input())
# The first while loop ensures that the user enters at least one number
# if, the user enters anything less than 1, it will prompt the user to enter something greater than one

while num_int < 1:
    print("Please enter at least one number")
    num_int = int(input())
else:
    print("Please enter", num_int, "numbers.")

    first_int = int(input())
    #  the first number is the largest as well as the smallest number
    min = first_int
    max = first_int

    # if the number of ints requested by user is greater than one, we'll initialize
    # a while loop

    while num_int > 1:
        n = int(input())
        if n < min:
            min = n
        if n > max:
            max = n

        num_int -= 1

    print("min:", min)
    print("max:", max)
