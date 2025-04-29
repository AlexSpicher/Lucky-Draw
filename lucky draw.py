import random

draw = random.randint(1, 1000000)

guess = int(input('Choose a number between 1 and 1000000: '))

if draw == guess:
    print('You win!')

if draw != guess:
    print('Sorry, try again')