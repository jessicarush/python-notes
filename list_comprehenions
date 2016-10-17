# List Comprehensions

# You could build a list of integers like this:
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)

# or use and iterator and range() like this:
number_list = []
for number in range(1,6):
    number_list.append(number)

# or turn the output of range directly into a list:
number_list = list(range(1,6))

# or use list comprehensions: 
# [expression for item in iterable]
number_list = [number for number in range(1,6)]

# The expression starts the list, the item is part of the for loop
number_list = [number+3 for number in range(0,5)]

# List comprehension with conditionals:
# [expression for item in iterable if condition]
number_list = [number for number in range (1,10) if number % 2 == 1]

# The above is the same as:
number_list = []
for number in range(1,10):
    if number % 2 == 1:
        number_list.append(number)
        
        
        
        
        
        
        

# Nested loops. Traditional way:
rows = range(1,4)
cols = range(1,3)

for row in rows:
    for col in cols:
        print (row, col)

# OR Assign to a variable making a list of (row, col) tuples:
rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

# Use tuple unpacking to pull the row an col values from each tuple:

for row, col in cells:
    print(row, col)
