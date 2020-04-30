#guessing game based on while loop
import random
n = 20
guess = int(n*random.random()) +1

gs = 0
while gs != guess:
    gs = int(input('Enter the number: '))
    if gs > 0:
        if gs > guess:
            print('number too large')
        elif gs < guess:
            print('number too small')
    else:
        print('Sorry to know that you are giving up!')
        break
else:
    print('congratulation you made it')


