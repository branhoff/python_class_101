import random
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

rand_num = random.randint(1, 100)
num_guesses = 0
old_guess = 0

while True:
    try:
        guess = int(input('Enter your guess: '))
        num_guesses += 1

        if guess < 1 or guess > 100:
            print(f'{Fore.RED}OUT OF BOUNDS!')
        
        elif guess == rand_num:
            print(f'{Fore.GREEN}CORRECT GUESS! Took {num_guesses} tries!')
            break
        
        elif abs(guess - rand_num) <= 10:
            if old_guess == 0:
                print(f'{Fore.CYAN}WARM!')
            
            elif abs(guess - rand_num) < abs(old_guess - rand_num):
                print(f'{Fore.CYAN}WARMER!')
            
            elif abs(guess - rand_num) > abs(old_guess - rand_num):
                print(f'{Fore.CYAN}COLDER!')
            
            else:
                print(f'{Fore.RED}PLEASE ENTER A NEW GUESS!')
        
        else:
            if old_guess == 0:
                print(f'{Fore.CYAN}COLD!')
            
            elif abs(guess - rand_num) < abs(old_guess - rand_num):
                print(f'{Fore.CYAN}WARMER!')
            
            elif abs(guess - rand_num) > abs(old_guess - rand_num):
                print(f'{Fore.CYAN}COLDER!')

            else:
                print(f'{Fore.RED}PLEASE ENTER A NEW GUESS!')

        old_guess = guess
        
    except:
        print(f'{Fore.RED}Please enter an integer and try again.')
