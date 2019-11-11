print ('Please guess a number between 1 and 5.')
guess = input()
guess = int(guess)
import random
from random import randint
answer = (randint(1,6))
if guess == answer:
    print ('congrats your guess is right!')
    elif guess < answer:
        print ('guess higher')
        guess = input()
        if guess == answer:
        print ('congrats your guess is right!')
    elif guess > answer:
        print ('guess lower')
        guess = input()
        if guess == answer:
        print ('congrats your guess is right!')
        elif guess < answer:
        print ('guess higher')
        elif guess > answer:
        print ('guess lower')


