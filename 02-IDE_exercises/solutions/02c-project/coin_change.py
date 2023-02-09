# Author: Brandon Hoffman
# Date: 09/24/2020
# Description: Asks the user for int  of cents less than $1 and returns
#              breakout of coin denominations with fewest number of coins
# Hint: the floor division // could be useful where it rounds the result down to the nearest whole number
# or the modulo operator can also be used.

print("Please enter an amount between 0 and 99 cents.")

coins: int = int(input())

print("Your change will be:")

quarters: int = coins // 25
coins -= quarters * 25
dimes: int = coins // 10
coins -= dimes * 10
nickels: int = coins // 5
coins -= nickels * 5
pennies: int = coins

print("Q:", quarters)
print("D:", dimes)
print("N:", nickels)
print("P:", pennies)