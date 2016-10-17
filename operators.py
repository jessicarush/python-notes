# OPERATORS

a = 4
b = 5

# Arithmetic operators

print(a + b) # Add
print(a - b) # Subtract
print(a * b) # Multiply
print(a / b) # Divide
print(a // b) # Floor division: digits after the decimal are dropped
print(a % b) # Modulus: divides and returns the remainder
print(a ** b) # Exponent calculation

# Comparison operators

print(a > b) # Greater than
print(a < b) # Less than
print(a >= b) # Greater or equal to
print(a <= b) # Less or equal to
print(a == b) # Equal to
print(a != b) # Not equal to

# Assignment operators

a = b # Assigns the values from the right to the left
print(a)
a += b # Equivalent to a = a + b
print(a)
a -= b # Equivalent to a = a - b
print(a)
a *= b # Equivalent to a = a * b
print(a)
a /= b # Equivalent to a = a / b
print(a)
a //= b # Equivalent to a = a // b
print(a)
a %= b # Equivalent to a = a % b
print(a)
a **= b # Equivalent to a = a ** b
print(a)

# Get // and % with divmod()

c = divmod(a, b) # will return the quotient and the remainder as a tuple
print(c)
print(type(c))
