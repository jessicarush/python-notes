'''True False Logic'''

# True
# False
# and
# or
# in
# is
# not
# not ... or
# not ... and
# not in
# is not
# ==
# !=
# >=
# <=

# Any 'and' expression that has a False is immediately False
# Any 'or' expression that has a True is immediately True

print(not False)                # True
print(not True)                 # False
print(True or False)            # True
print(True or True)             # True
print(False or True)            # True
print(False or False)           # False
print(True and False)           # False
print(True and True)            # True
print(False and True)           # False
print(False and False)          # False
print(not (True or False))      # False
print(not (True or True))       # False
print(not (False or True))      # False
print(not (False or False))     # True
print(not (True and False))     # True
print(not (True and True))      # False
print(not (False and True))     # True
print(not (False and False))    # True
print(1 != 0)                   # True
print(1 != 1)                   # False
print(0 != 1)                   # True
print(0 != 0)                   # False
print(1 == 0)                   # False
print(1 == 1)                   # True
print(0 == 1)                   # False
print(0 == 0)                   # True
