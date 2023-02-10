# Author: Brandon Hoffman Date: 10/17/2020 Description: created a function called fib() that calculate a Fibonacci
# number for a given 'n' without recursion or the golden ratio.


def fib(n) -> int:
    """calculate a fibonnaci number given the input 'n' without recursion using the golden ratio"""

    prev_num: int = 0
    curr_num: int = 1
    sol: int = 1
    print("The numbers in fibonacci series are : ")
    i:  int
    for i in range(n - 1):
        sol = curr_num + prev_num
        prev_num = curr_num
        curr_num = sol
        print(sol)
    return sol


number: int = int(input("Please enter a number to calculate its Fibonacci number: "))
print("The Fibonacci number is: ", fib(number))
