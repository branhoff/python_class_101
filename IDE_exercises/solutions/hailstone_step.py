# Author: Brandon Hoffman
# Date: 10/17/2020
# Description: Wrote a function for a hailstone sequence where a given number, if even is divided by two and if odd is multiplied by 3 and added by 1. The result will go through the 
#              same process until the result terminates at a value of 1.


def hailstone(n):
    '''takes an integer, 'n' and if even divides by 2 and if odd multiples by 3 and adds 1
       the result continues until the value reaches 1 and the function terminates and returns the count the number of steps'''
    count = 0
    while n != 1:
        print(count, n)
        if n % 2 == 0:
            n //= 2
        else:
            n = (n * 3) + 1
            
        count += 1

    return count