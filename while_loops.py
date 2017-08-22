# While loop with break, continue examples

def test1():
    while True:
        stuff = input('Capitalize text [type q to quit]: ')
        if stuff == 'q':
            break
        else:
            print(stuff.capitalize())

def test2():
    while True:
        value = input('Interger [q to quit]:')
        if value == 'q':
            break
        try:
            number = int(value)
        except ValueError:
            continue
        number = int(value)
        print(number, 'squared is', number * number)

test1()
test2()
