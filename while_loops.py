'''While loops with break and continue'''

# while is a looping mechanism that's used with if, elif, else or try. A while
# loop will loop forever unless you, break, continue, pass or return something.
# Break is useful when you want to terminate the loop early if some condition
# is met. Continue is for when you want to skip past an iteration to the next.


x = 10
while x > 0:
    print(x)
    x -= 1
    if x == 5:
        break

# Example using if, elif, else, break and continue ----------------------------

import random

print('Guess a number between 1 and 10 (0 to quit)')

answer = random.randint(1, 9)

while True:
    guess = (int(input('> ')))
    if guess != answer:
        if guess == 0:
            print('bye')
            break
        elif guess > answer:
            print('No, lower')
            continue
        else:
            print('No, higher')
            continue
    else:
        print('You guessed it!')
        break

# Example using if, try, break, continue --------------------------------------

def squared():
    while True:
        value = input('Integer [q to quit]:')
        if value == 'q':
            break
        try:
            number = int(value)
        except ValueError:
            print("That's not an integer")
            continue
        number = int(value)
        print(number, 'squared is', number * number)

squared()

# Example using try and return ------------------------------------------------

print('Enter two numbers please.')

def get_inputs(arg):
    while True:
        try:
            x = input('enter {} number: '.format(arg))
            x = int(x)
            return x
        except:
            print('I need an integer please')

a = get_inputs('first')
b = get_inputs('second')

print('{} * {} = {}'.format(a, b, a * b))
