# Author: Brandon Hoffman
# Date: 10/17/2020
# Description: Wrote a function for a hailstone sequence where a given number is divided by two if even and is multiplied by 3 and added by 1 if odd.
#              This process wil repeat itself until the given number is transformed into 1. Should return the count of steps to achieve this.


def hailstone(n):
    """
    takes an integer, 'n' and if even divides by 2. If odd multiples by 3 and adds 1
    the result continues until the value reaches 1 and the function terminates and returns the count of iterations or steps
    """
    count = 0
    while n != 1:
        print(count, n)
        if n % 2 == 0:
            n //= 2
        else:
            n = (n * 3) + 1
            
        count += 1

    return count