'''While loops with break and continue'''

# while is a looping mechanism that's used with if, elif, else

# break is useful when you want to terminate the loop early if some condition
# is met.

# continue is useful for when you want to skip past in iteration to the next.

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

# Another example -------------------------------------------------------------

def squared():
    while True:
        value = input('Integer [q to quit]:')
        if value == 'q':
            break
        try:
            number = int(value)
        except ValueError:
            continue
        number = int(value)
        print(number, 'squared is', number * number)

squared()

# And Another -----------------------------------------------------------------

x = 10
while x > 0:
    print(x)
    x -= 1
    if x == 5:
        break
