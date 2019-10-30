'''Operators'''


a = 4
b = 5


# Arithmetic operators
# -----------------------------------------------------------------------------

print(a + b)   # Add
print(a - b)   # Subtract
print(a * b)   # Multiply
print(a / b)   # Divide
print(a // b)  # Floor division: digits after the decimal are dropped
print(a % b)   # Modulus: divides and returns the remainder of the first number
print(a ** b)  # Exponent calculation


# Comparison operators
# -----------------------------------------------------------------------------

print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater or equal to
print(a <= b)  # Less or equal to
print(a == b)  # Equal to
print(a != b)  # Not equal to


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

c = divmod(a, b)  # will return the quotient and the remainder as a tuple
print(c)          # (0, 4)
print(type(c))    # <class 'tuple'>

# NOTE: when working with modulus or divmod, keep in mind that when dividing
# a larger number into a smaller number, the quotient will be always be zero
# and the remainder will be the first number. This may seem obvious but still
# worth noting.


# Walrus operator :=
# -----------------------------------------------------------------------------
# New to Python 3.8 and the thing we lost Guido over, the walrus operator
# allows you to make and assignment and use the result at the same time.

# For example:

a = [1, 2, 3, 4, 5, 6, 7]

# Without walrus:

if (len(a)) > 5:
    print(f'List too long (expected 5, got {len(a)}).')
    # List too long (expected 5, got 7).

# With walrus:

# if (n := len(a)) > 5:
    # print(f'List too long (expected 5, got {n}).')
    # List too long (expected 5, got 7).

# Another example use case could be a list comprehensions where
# a value computed in the filtering condition is also needed in
# the expression body. In other words, share a subexpression
# between a comprehension filter clause and its output.

# For example:

# Without walrus

# With walrus:
# filtered_data = [y for x in data if (y := f(x)) is not None]

# A loop that can't be trivially rewritten using 2-arg iter()
# while chunk := file.read(8192):
   # process(chunk)
