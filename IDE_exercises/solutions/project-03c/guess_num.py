# Author: Brandon Hoffman
# Date: 10/05/2020
# Description: Guessing game that takes a number to guess and has user contiously 
#              make guesses till they get the answer correct

print("Enter the number for the player to guess.")
solution = int(input())

print("Enter your guess.")
guess = int(input())

number_of_guesses = 1

while guess != solution:
    if guess > solution:
        print("Too high - try again:")
        guess = int(input())
    if guess < solution:
        print("Too low - try again:")
        guess = int(input())

    number_of_guesses += 1

number_of_guesses +=1

print("You guessed it in", number_of_guesses, "tries.")