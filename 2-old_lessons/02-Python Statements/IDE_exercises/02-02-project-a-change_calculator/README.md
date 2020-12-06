# 00-02-project-b

Let's enhance our change calculator from before. We need to account for mistakes our user might make so our code won't crash.
Update a program that asks the user for a (integer) number of cents, from 0 to 99, and outputs how many of each type of coin would represent that amount with the fewest total number of coins as before.  
However, also add in checks to make sure all of our assumptions are met.
When you run your program, it should match the following format:

For example, if the amount is greater than 99, the program should not run it should return a message. such as:
```
Please enter an amount in cents less than a dollar.
106
Must be less than a dollar
```
Otherwise it should run as it was originally intended:
'''
Please enter an amount in cents less than a dollar.
87
Your change will be:
Q: 3
D: 1
N: 0
P: 2
```
Hint: There are several assumptions our code is expecting our user to follow. Try to account for all of them

Note for international students:
* 1 quarter = 25 cents
* 1 dime = 10 cents
* 1 nickel = 5 cents
* 1 penny = 1 cent


