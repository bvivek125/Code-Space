#!/usr/bin/env python 
from __future__ import print_function, unicode_literals

### Exercise 1:
'''Write a function (guessing_game) that takes no arguments.
When run, the function chooses a random integer between 0 and 100 (inclusive).
Then ask the user to guess what number has been chosen.
Each time the user enters a guess, the program indicates one of the following:
Too high
Too low
Just right
If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
The program only exits after the user guesses correctly.

We’ll use the randint function in the random module to generate a random number.
randint(self, a, b) - Return random integer in range [a, b], including both end points.'''


import random
def guessing_game():
    name = input("Enter your name: ")
    print(f'Hey {name}!, welcome to play the guessing game')
    print(''*50)
    print('-'*50)
    random_number = random.randint(0,100)
    print(f'The random number generated is, {random_number}')
    while True:
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

