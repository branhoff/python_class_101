# project-04c

A hailstone sequence begins with a positive integer. 
If the integer is even, divide it by two to get the next integer in the sequence, but if it is odd, multiply it by three and add one to get the next integer in the sequence. 
Then you use the value you just generated to find the next value, according to the same rules.  
For example, if our initial number is 3, the subsequent numbers will be: 10, 5, 16, 8, 4, 2, 1.

Write a Python function called hailstone_step(num) that takes a positive number as parameter for the initial number of a hailstone sequence and returns how many steps it takes to reach 1, you must stop once you have reached 1.
If the starting integer is 1, the return value should be 0, since it takes no steps to reach 1. 
For example, if the starting number is 3, then the sequence would go: 3, 10, 5, 16, 8, 4, 2, 1, and the result should be 7, since it took 7 steps to reach 1. 
Don't print anything out, just return a value

For example, your function could be used like this:
```
answer = hailstone_step(1000)
print(answer)
```

You cannot use recursion, since we haven't covered that technique.

The file should be named: **hailstone_step.py**
