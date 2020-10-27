# Author: Brandon Hoffman
# Date: 10/05/2020
# Description: Take in positive integer and print list of factors

integer = int(input("Please enter a positive integer: "))
print("The factors of", integer, "are:")

for i in range(1, integer+1): # the README states we want to include all the factors of the input including 1 and the, so we'll need to structure range with two arguments
    if integer % i == 0:
        print(i)