
from colorama import init, Fore

init(convert=True, autoreset=True)


print(Fore.GREEN + '*'*90 + '\n' + ' '*33 + 'Guessing Game Challenge' + '\n' + '*'*90)
print(f'{Fore.CYAN}Rules: \n\
-Guess a number from 1-100 until you get the correct number \n\
-If your guess is less than 1 or greater than 100, you will get "OUT OF BOUNDS!" \n\
-On your first turn, if your guess is within 10 of the number, you will get "WARM!", \n\
    otherwise you will get "COLD!" \n\
-On subsequent guesses, if your guess is closer to the number than your previous guess, \n\
    you will get "WARMER!", otherwise you will get "COLDER!" \n\
-When you correctly guess the number, you will get "CORRECT GUESS!" with the number of \n\
    tries it took \n')

input('Press enter to start the game.')


import random

answer = random.randint(1, 100)

guess = int(input("\nTake a guess from 1 to 100: "))

guesses = []


while guess != answer:
    diff = guess - answer
    guesses.append(guess)
    good_guesses = [g for g in guesses if g <= 100 and g >= 1]

    print()
    if guess > 100 or guess < 1:
        print('OUT OF BOUNDS')
    
    if (guess > 100 or guess < 1) and len(good_guesses) > 1:
        print(f'Your last good guess was {good_guesses[-1]}')

    elif len(good_guesses) == 1:
        if abs(diff) <= 10:
            print('WARM!')
        else:
            print('COLD!')
    
    elif len(good_guesses) > 1:
        if abs(answer - good_guesses[-1]) < abs(answer - good_guesses[-2]):
            print('WARMER...')
        else:
            print('COLDER...')

    guess = int(input("Take another guess: "))

print(f'You got it! It only took you {len(guesses)} attempts...')





