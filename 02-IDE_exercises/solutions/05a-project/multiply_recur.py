# Author: Brandon Hoffman
# Date: 10/24/2020
# Description: write a function that uses recursive iteration to multiply two positive integers
#              with addition

def multiply(multiplier, multiplicand) -> int:
    """
    Takes in two positive integers and multiplies them by recursively adding the int multiplicand int multiplier times.
    """
    if multiplier == 1:
        return multiplicand
    else:
        return multiply(multiplier - 1, multiplicand) + multiplicand


multiplier: int = int(input("Please enter a multiplier: "))
multiplicand: int = int(input("Please enter a multiplicand: "))
print("The result is: ", multiply(multiplier, multiplicand))
