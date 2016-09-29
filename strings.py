# Working with strings

# .replace()

name = 'Yello'
name = name.replace('Y', 'H')
print(name)

# Slice with [start : end : step]

letters = 'abcdefghijk'
print(letters[:])
print(letters[2:])
print(letters[2:10])
print(letters[:10])
print(letters[2:10:2])

# Split
test_string = "Yeti, Bigfoot, Loch Ness, Unicorn..."
test_list = test_string.split()
print(test_list)
print(type(test_list))

# Join
test_string = ' '.join(test_list)
print(test_string)
print(type(test_string))

# Things you can check with strings
print(test_string[:5])
print(len(test_string))
print(test_string.startswith('Yeti'))
print(test_string.endswith('Yeti'))

word = 'Ness'

print(test_string.find(word))
print(test_string.rfind(word))
print(test_string.count(word))
print(test_string.isalnum())

# remove from the beginning and end:
test_string = test_string.strip('.')
print(test_string)

# replace haracters or words:
# you can also use a number argumen to limit the number of replacements:
# like this: test_string.replace(',', '', 2)
test_string = test_string.replace(',', '')
print(test_string)

# change case:
test_string = test_string.lower()
print(test_string)

test_string = test_string.capitalize()
print(test_string)

test_string = test_string.title()
print(test_string)

test_string = test_string.upper()
print(test_string)

test_string = test_string.swapcase()
print(test_string)

# alignemnt:
test_string = test_string.center(60)
print(test_string)

test_string = test_string.ljust(60)
print(test_string)

test_string = test_string.rjust(60)
print(test_string)

test_string = test_string.replace('unicorn', 'redbull')
print(test_string)
