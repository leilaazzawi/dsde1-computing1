print ('Please guess a number between 1 and 5.')
guess = input()
guess = int(guess)
import random
from random import randint
answer = (randint(1,5))
if guess == answer:
    print ('congrats your guess is right!')
else:
    print ('Sorry you guessed wrong.')
    print ('You have two more attempts, guess again.')
    guess = input()
    if guess == answer:
        print ('Yay! That is correct.')
    else:
        print ('Incorrect! You have one more attempt, guess again.')
        guess = input()
        if guess == answer:
            print ('Finally!')
        else:
            print ('You have failed.')