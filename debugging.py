'''Debugging'''

# print the values of your local arguments with:

# print(vars())

# NOTE: if you run your program with an -i flag, it will drop you into the
# interactive interpretor if the program fails:

# pyhton3 -i myfile.py

# Bug test: read a file of countries and their capital cities, separated by a
# comma, and write them out as capital, country. In addition:
# Make sure they capitalized incorrectly
# Remove any extra spaces extra spaces
# Stop the program if we find the word quit (uppercase or lowercase)

# Here’s a sample data file cities1.csv:
'''
France, Paris
 Venuzuela,Caracas
  LithuniA,Vilnius
    quit
'''

# Here's pseudocode:
'''
for each line in the text file:
    read the line
    strip leading and trailing spaces
    if 'quit' occurs in a lowercase copy of the line:
        stop
    else:
        split the country and capital by the comma character
        trim any leading and trailing spaces
        convert the country and capital to titlecase
        print the capital, a comma, and the country
'''

def process_cities(filename):
    with open(filename, 'rt') as file:
        for line in file:
            line = line.strip()
            if 'quit' in line.lower(): # should be if 'quit' == line.lower():
                return                     
            country, city = line.split(',')
            city = city.strip()
            country = country.strip()
            print(city.title(), country.title(), sep=',')

import pdb; pdb.set_trace() # this will launch the debugger
process_cities('cities2.csv')

# type 'c' to continue once it starts
# type 's' single step through lines (this will include any modules you
# might be using like sys)
# type 'n' to step but not go inside functions.
# Generally speaking you would 'n' to step past any library code
# type 'l' to see the next few lines at once
# type 'll' to see even more of the next few lines at once
# type 'l' and a line number to see lines from that point
# type 'b' and a line number to insert a breakpoint
# type 'b' alone to see all your breakpoints
# Your program will ONLY stop at a breakpoint if it has a chance to actually
# get to that spot in the code.
# type 'u' to go up (back)
# 'p' to print the value of something. i.e. p line
# or you can just type a variable name and it will output its current value
# when viewing lines, 'B' indicates a breakpoint you've inserted and
# '->' indicates your current line
# Type help when in the pdp to see all the commands. Type help command to get
# help on that one.

# To use the debugger from the command line, import the pdb module by typing:
# $ python -m pdb myfile.py
