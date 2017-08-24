'''While loops with break and continue'''

print('Guess a number between 1 and 10')

while True:
    guess = (int(input('> ')))
    if guess != 7:
        if guess > 7:
            print('No, lower')
            continue
        else:
            print('No, higher')
            continue
    else:
        print('You guessed it!')
        break

# Another example:

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

# And Another:

x = 10
while x > 0:
    print(x)
    x -= 1
    if x == 5:
        break
