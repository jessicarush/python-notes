'''Functions that convert data types'''

float(True)                                 # returns 1.0
int(True)                                   # returns 1
str(True)                                   # returns True
list((1,2,3))                               # returns [1, 2, 3]
dict((('a', 'A'), ('b', 'B'), ('c', 'C')))  # returns {'c':'C', 'a':'A', 'b':'B'}
set((('a'), ('b'), ('c')))                  # returns {'b', 'c', 'a'}
tuple((('a'), ('b'), ('c')))                # returns ('a', 'b', 'c')
