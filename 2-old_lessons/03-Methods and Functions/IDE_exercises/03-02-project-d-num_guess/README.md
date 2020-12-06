# 03-02-project-d

Let's reuse the one of our exercises from earlier, but add in "functions". So create or adapt the num_guess from earlier, but now we'll modularize it a bit. Let's write two functions, one called "main" and the other called "compare_guess". The compare_guess function will compare a guess to a given solution. It should accept two arguments. 1. an intial guess and 2. a solution.

The "main" function will house the steps. It won't have any arguments, but will ask the user for the intial input and the solution and then pass that information as arguments to the compare_guess function. Only the main function should be called in the global scope, to run the entire process and get the desired result.

Here's some adapted instructions:

The main functioun should prompt the user for an integer that the player (maybe the user, maybe someone else) will try to guess and prompt you for a solution (obviously a terrible game). The "compare_guess" function should compare if the player's guess is higher than the target number, the program should display "too high"  If the user's guess is lower than the target number, the program should display "too low"  The program should use a loop that repeats until the user correctly guesses the number.  Then the program should print how many guesses it took and return the number of guesses.  When you run your program it should match the following format:
```
Enter the number for the player to guess.
-12
Enter your guess.
100
Too high - try again:
50
Too high - try again:
-2000
Too low - try again:
-12
You guessed it in 4 tries.
```
If the user guesses the number in 1 try, then your program should print "You guessed it in 1 try." and return the number 1.


