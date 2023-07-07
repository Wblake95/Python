#!/bin/env python

import random

randomInt=random.randint(1,10)
guessCount=0

while True:
    guess=int(input('Guess a number between 1 and 10!'))
    guessCount+=1
    if guess==randomInt:
        print('Great job!',guess,'was correct!')
        print('You were able to guess in',guessCount,'guesses!')
        break
    elif guess<randomInt:
        print('Your guess is to low')
        continue
    else:
        print('Your guess was to high')
        continue
