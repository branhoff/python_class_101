# Author: Brandon Hoffman
# Date: 09/24/2020
# Description: Asks the user for int  of cents less than $1 and returns
#              breakout of coin denominations with fewest number of coins. Checks for Errors.

print("Please enter an amount in cents less than a dollar.")

coins = int(input())

if coins < 0 :
    print("ERROR: Your input must be a non-negative number less than 100")

elif coins >= 100:
    print("ERROR: Your input must be a non-negative number less than 100")

else:
    print("Your change will be:")

    quarters = coins // 25
    remainder = coins % 25
    dimes = remainder // 10
    remainder %=  10
    nickels = remainder // 5
    remainder %= 5
    pennies = remainder

    print("Q:", quarters)
    print("D:", dimes)
    print("N:", nickels)
    print("P:", pennies)