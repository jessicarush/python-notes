# Dictionary comprehensions
# { key_expression : value_expression for expression in iterable}

word = 'letters'
letter_counts = {letter : word.count(letter) for letter in word}

print(letter_counts)

# Technically we are counting some letters twice.
# By converting the word into a set(), we remove any duplicates for the checking part

word = 'letters'
letter_counts = {letter : word.count(letter) for letter in set(word)}

print(letter_counts)
