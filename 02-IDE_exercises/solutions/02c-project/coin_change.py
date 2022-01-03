# Author: Brandon Hoffman
# Date: 09/24/2020
# Description: Asks the user for int  of cents less than $1 and returns
#              breakout of coin denominations with fewest number of coins

print("Please enter an amount between 0 and 99 cents.")

coins = int(input())

print("Your change will be:")

quarters = coins // 25
coins -= quarters * 25
dimes = coins // 10
coins -= dimes * 10
nickels = coins // 5
coins -= nickels * 5
pennies = coins

print("Q:", quarters)
print("D:", dimes)
print("N:", nickels)
print("P:", pennies)