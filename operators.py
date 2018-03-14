'''Operators'''

a = 4
b = 5


# Arithmetic operators
# -----------------------------------------------------------------------------

print(a + b)  # Add
print(a - b)  # Subtract
print(a * b)  # Multiply
print(a / b)  # Divide
print(a // b) # Floor division: digits after the decimal are dropped
print(a % b)  # Modulus: divides and returns the remainder of the first number
print(a ** b) # Exponent calculation


# Comparison operators
# -----------------------------------------------------------------------------

print(a > b)  # Greater than
print(a < b)  # Less than
print(a >= b) # Greater or equal to
print(a <= b) # Less or equal to
print(a == b) # Equal to
print(a != b) # Not equal to


# Assignment operators
# -----------------------------------------------------------------------------

a = b     # Assigns the values from the right to the left
print(a)  # 5
a += b    # Equivalent to a = a + b
print(a)  # 10
a -= b    # Equivalent to a = a - b
print(a)  # 5
a *= b    # Equivalent to a = a * b
print(a)  # 25
a /= b    # Equivalent to a = a / b
print(a)  # 5.0
a //= b   # Equivalent to a = a // b
print(a)  # 1.0
a %= b    # Equivalent to a = a % b
print(a)  # 1.0
a **= b   # Equivalent to a = a ** b
print(a)  # 1.0


# Get // and % with divmod()
# -----------------------------------------------------------------------------

a = 4
b = 5

c = divmod(a, b) # will return the quotient and the remainder as a tuple
print(c)         # (0, 4)
print(type(c))   # <class 'tuple'>

# NOTE: when working with modulus or divmod, keep in mind that when dividing
# a larger number into a smaller number, the quotient will be always be zero
# and the remainder will be the first number. This may seem obvious but still
# worth noting.
