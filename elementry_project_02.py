
#number_guessing_game

import random

number_to_guess = random.randint(1,100)

while True:
    
    try:
        
        guess = int(input('guess the number = '))
        
        if guess < number_to_guess:
            print('too low')
        elif guess > number_to_guess:
            print('too high')
        else:
            print('congratulations! you guessed the number')
            break
        
    except ValueError:
        print('please enter a valid number')