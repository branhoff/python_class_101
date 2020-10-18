# project-4b

The first and second numbers in the Fibonacci sequence are both 1.  After that, each subsequent number is the sum of the two preceding numbers.  The first several numbers in the sequence are: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, etc.  Write a function named fib that takes a positive integer parameter and returns the number at that position of the Fibonacci sequence.  For example fib(1) = 1, fib(3) = 2, fib(10) = 55, etc.  Your function does not need to print anything out - just return a value.

For example, your function could be called like this:
```
term = fib(17)
```

You cannot use recursion, since we haven't covered that technique.  That means that for this assignment you cannot have your function call itself.  You must use a loop to step through the sequence - do not use the golden ratio to directly calculate the value.

The file must be named fib.py
