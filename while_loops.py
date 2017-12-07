'''While loops, break and continue'''

# while is a looping mechanism that's used with if, elif, else or try. A while
# loop will loop forever unless you, break, continue, pass or return something.
# Break is useful when you want to terminate the loop early if some condition
# is met. Continue is for when you want to skip past an iteration to the next.

x = 5
while x > 0:
    x -= 1
    if x == 2:
        break
    print(x)
# 4
# 3

x = 5
while x > 0:
    x -= 1
    if x == 2:
        continue
    print(x)
# 4
# 3
# 1
# 0

# -----------------------------------------------------------------------------
# Example using if, elif, else, break and continue
# -----------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------
# Example using if, try, break, continue
# -----------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------
# Example using try and return
# -----------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------
# A slightly different approach
# -----------------------------------------------------------------------------
# A 'flag' variable is a great way of signaling a while loop when you have
# many things that could/should end the loop. Using a flag variable, our loop
# only has to check one condition.

print('Kilograms to Pounds converter')
prompt = 'Enter kilos (q to quit): '
KILO_POUNDS = 2.20462
active = True  # this is a flag variable!

while active:
    value = input(prompt)
    if value == 'q':
        active = False
    else:
        try:
            new_value = int(value) * KILO_POUNDS
            print(value, 'kilograms is', new_value, 'pounds')
        except:
            print("I need a number or 'q' to quit: ")

# -----------------------------------------------------------------------------
# While Loops with Lists & Dicts
# -----------------------------------------------------------------------------
# A for loop is effective for iterating through a list but apparently, "You
# shouldn't modify a list inside a for loop because Python will have trouble
# keeping track of the items in the list. To modify a list as you work through
# it, use a while loop." Using a while loop allows you to better collect,
# store and organize.

unconfirmed_users = ['rick', 'morty', 'raja', 'bob']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Magical verification of user: {}'.format(current_user.title()))
    confirmed_users.append(current_user)

for user in confirmed_users:
    print('Confirmed user: {}'.format(user.title()))

# -----------------------------------------------------------------------------
# Filling a dict with user input
# -----------------------------------------------------------------------------
shopping_list = {}

while True:
    item = input('Item (q to quit): ')
    if item == 'q':
        break
    store = input('Store: ')
    if store in shopping_list:
        shopping_list[store].append(item)
    else:
        shopping_list[store] = [item]

if shopping_list:
    print('Shopping list\n')

for store, items, in shopping_list.items():
    print(store.title())
    for item in items:
        print('– ', item)
    print('-' * 25)
