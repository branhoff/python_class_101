# Author: Brandon Hoffman
# Date: 09/24/2020
# Description: Takes in 5 float or int values and calculates the average for the inputs

print("Please enter five numbers")
input_1: float = float(input())
input_2: float = float(input())
input_3: float = float(input())
input_4: float = float(input())
input_5: float = float(input())

avg: float = (input_1 + input_2 + input_3 + input_4 + input_5) / 5
print("The calculated average of those numbers is: " + str(avg))
