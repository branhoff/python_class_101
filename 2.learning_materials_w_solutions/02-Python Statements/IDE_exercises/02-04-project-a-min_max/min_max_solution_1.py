# Author: Brandon Hoffman
# Date: 10/04/2020
# Description: Take in number of integers to record from user. Return min and max
#              integers from user

print("How many integers would you like to enter?")
limit = int(input())
print("Please enter", limit, "integers.")

first_int = int(input())
min_val = first_int
max_val = first_int

count = 1

# if the number of ints requested by user is greater than one, we'll initialize
# a while loop
while count < limit:
    n = int(input())
    if n < min_val:
        min_val = n
    if n > max_val:
        max_val = n
    
    count += 1

print("min:", min_val)
print("max:", max_val)