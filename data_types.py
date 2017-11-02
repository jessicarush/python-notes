'''Functions that convert data types'''

float(True)                                 # -> 1.0
int(True)                                   # -> 1
str(True)                                   # -> True
list((1,2,3))                               # -> [1, 2, 3]
dict((('a', 'A'), ('b', 'B'), ('c', 'C')))  # -> {'c':'C', 'a':'A', 'b':'B'}
set((('a'), ('b'), ('c')))                  # -> {'b', 'c', 'a'}
tuple((('a'), ('b'), ('c')))                # -> ('a', 'b', 'c')
