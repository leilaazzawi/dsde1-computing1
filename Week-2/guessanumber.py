print ('Please guess a number between 1 and 10.')
guess = input()
guess = int(guess)
import random
from random import randint
print ('The real answer is', randint(1,10))
print ('Your guess was ' + str(guess == randint))