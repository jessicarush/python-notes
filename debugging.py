'''Debugging'''

# General Tips
# -----------------------------------------------------------------------------
# Though not very advanced, dropping print() statements and print(type())
# can tell you a lot about what's going on. Beyond that:

# print the values of your local arguments with:
print(vars())

# If you run your program with an -i flag, it will drop you into the
# interactive interpreter if the program fails:

# $ python3 -i myfile.py


# Standard Library: pdb module
# -----------------------------------------------------------------------------
# Bug test: read a file of countries and their capital cities, separated by a
# comma, and write them out as capital, country. In addition:
# – Make sure they capitalized incorrectly
# – Remove any extra spaces extra spaces
# – Stop the program if we find the word quit (uppercase or lowercase)

# Here's a sample data file data/cities.csv:
'''
France, Paris
 venuzuela,caracas
  LithuniA,vilnius
 argentina,buenos aires
  bolivia,la paz
  brazil,brasilia
  chile,santiago
  colombia,Bogotá
  ecuador,quito
  falkland islands,stanley
french guiana,cayenne
guyana,georgetown
 paraguay,Asunción
 peru,lima
suriname,paramaribo
uruguay,montevideo
venezuela,caracas
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

# Here's the actual code:
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

import pdb; pdb.set_trace()  # this will launch the debugger

process_cities('data/cities.csv')


# pdb Commands
# -----------------------------------------------------------------------------
# Documented commands (type help <topic>):

# EOF    c          d        h         list      q        rv       undisplay
# a      cl         debug    help      ll        quit     s        unt
# alias  clear      disable  ignore    longlist  r        source   until
# args   commands   display  interact  n         restart  step     up
# b      condition  down     j         next      return   tbreak   w
# break  cont       enable   jump      p         retval   u        whatis
# bt     continue   exit     l         pp        run      unalias  where

# type 'c' to continue (the program will run until it ends normally or via
#          an Error/Exception). If it ends normally, we now it's logic error
#          rather than a syntax error.
# type 's' single step through lines and into functions/methods
#          (this will include any modules you might be using like sys)
# type 'n' to step past a function/method (execute and move onto the next).
#          Generally speaking you would 'n' to step past any library code.
# type 'l' to see the next few lines at once
# type 'll' to see even more of the next few lines at once
# type 'l' and a line number to see lines from that point onward
# type 'b' and a line number to insert a breakpoint
# type 'b' alone to see all your breakpoints
# type 'cl' and a number to (clear) a breakpoint

# NOTE: Your program will ONLY stop at a breakpoint if it has a chance to
# actually get to that spot in the code.

# type 'u' to go up (back)
# type 'p' to print the value of something. i.e. p line
# type a variable name and it will output its current value
# type '?' or help when in the pdb to see all the commands.
# type help command to get help on that one.

# NOTE: when viewing lines, 'B' indicates a breakpoint you've inserted and
# '->' indicates your current line

# To use the debugger from the command line, import the pdb module by typing:
# $ python3 -m pdb myfile.py

# For the example above if we drop a breakpoint at line 68 and continue our
# program, when it stops if we type line to see the current value of line we
# see our problem: ecuador,quito.
