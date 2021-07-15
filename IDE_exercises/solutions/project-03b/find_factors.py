# Author: Brandon Hoffman
# Date: 10/05/2020
# Description: Take in positive integer and print list of factors

integer = int(input("Please enter a positive integer:"))
print("The factors of", integer, "are:")

for i in range(1, integer+1):
    if integer % i == 0:
        print(i)