#!/usr/bin/env python 
from __future__ import print_function, unicode_literals

import random
def guessing_game():
    name = input("Enter your name: ")
    print(f'Hey {name}!, You have 3 chances to guess a number')
    print(''*50)
    print('-'*50)
    random_number = random.randint(0,100)
    #print(f'The random number generated is, {random_number}')
    for i in range(3):
        guess = input("Hey! Guess a number between 0 and 100:")
        if guess.isdigit(): 
            if (int(guess)<=100 or (int(guess)>=0 and int(guess)<100)):
                if int(guess) == random_number:
                    print(f'You got the number right!')
                    break
                elif int(guess) > random_number:
                    print(f'{guess} is too high; try again')
                else:
                    print(f'{guess} is too low; try again')
            else:
                print(f'Hello {name}!, Please enter a number between 0 & 100')
        else:
            print(f'Hello {name}!, Please enter an integer as an input')      
    print('-'*50)
    print(''*50)
guessing_game()