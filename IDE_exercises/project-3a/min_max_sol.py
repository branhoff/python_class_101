# Author: Brandon Hoffman
# Date: 10/04/2020
# Description: Take in number of integers to record from user. Return min and max
#              integers from user

print("How many integers would you like to enter?")
num_int = int(input())
print("Please enter", num_int, "integers.")

first_int = int(input())
min = first_int
max = first_int

count = 1

# if the number of ints requested by user is greater than one, we'll initialize
# a while loop
while count < num_int:
    n = int(input())
    if n < min:
        min = n
    if n > max:
        max = n
    
    count += 1

print("min:", min)
print("max:", max)