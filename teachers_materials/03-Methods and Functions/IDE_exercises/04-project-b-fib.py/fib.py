# Author: Brandon Hoffman
# Date: 10/17/2020
# Description: created a function called fib() that calculate a fibonnaci number for a given 'n' without recursion or the golden ratio.

def fib(n):
    '''calculate a fibonnaci number given the input 'n' without recursion using the golden ratio'''

    prev_num = 0
    curr_num = 1
    sol = 1
    for i in range(n-1):
        sol = curr_num + prev_num
        prev_num = curr_num
        curr_num = sol


    return sol

