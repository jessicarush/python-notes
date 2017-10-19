'''If Statements and Conditional Tests'''

# At the heart of every if statement is an expression that can be evaluated as
# True or False and this is called a conditional test (also called a boolean
# expression). If the conditional Test evaluates as True, python will execute
# the code following the if statement, otherwise it will be ignored.

cars = ['ford', 'bmw', 'honda', 'subaru']

# checking for equality:
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# checking for inequality:
for car in cars:
    if car != 'bmw':
        print(car.title())
    else:
        print(car.upper())

# Both produce the same result:
# Ford
# BMW
# Honda
# Subaru

# if, elif, else chains -------------------------------------------------------

age = 42

if age < 5:
    admission = 0
elif age < 19:
    admission = 5
elif age >= 65:
    admission = 3
else:
    admission = 10

print(admission)

# Note you are not required to have a final else statement. It may be more
# readable to use another elif. Keep in mind if you do it this way, there is no
# catchall at the end, so the value must meet one of the elif conditions or it
# may raise an exception.

if age < 5:
    admission = 0
elif age < 19:
    admission = 5
elif age >= 65:
    admission = 3
elif age < 65:
    admission = 10

# Check for values with in, not in --------------------------------------------

users = ['rick', 'morty', 'raja', 'bob']
user = 'morty'

if user in users:
    print('Hello', user.title())
else:
    print('Create account')

# same as:
if user not in users:
    print('Create account')
else:
    print('Hello', user.title())

# Check for multiple conditions -----------------------------------------------

import time

now = time.localtime()                # <class 'time.struct_time'>
day = time.strftime('%A', now)        # <class 'str'>
hour = int(time.strftime('%H', now))  # <class 'int'>

if (4 > hour or hour > 20) and (day != 'Friday') and (day != 'Saturday'):
    print('Time for bed!')
else:
    print('Carry on.')
