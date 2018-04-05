'''Shelve Module'''

# The shelve module can be used as a simple persistent storage option for
# Python objects when a relational database is overkill. The shelf is accessed
# by keys, just as with a dictionary. The values are pickled and written to a
# database file.

# When using modules like pickle, the downside is that all the data has to be
# loaded back using memory. This doesn't work so well for very large data
# structures. The shelve module is good for when dealing with large amounts of
# data. It stores the data on a "shelf" in a file rather than in memory. The
# shelf contains key value pairs like a dictionary. The keys should be a string
# and the values can be anything that can be pickled. All the methods you can
# use with a dictionary, can be used with shelf objects. Use the same caution
# with shelves as you would with pickle: no untrusted sources.


# shelve.open()
# -----------------------------------------------------------------------------
# Note: keys & values can only be added to shelves via individual assignments:

import shelve

with shelve.open('plants_shelf') as plants:
    plants['succulent'] = "a kind of cactus"
    plants['spider'] = "long slender leaves"
    plants['fern'] = "grows well in the forest"
    plants['yucca'] = "sharp stiff leaves"

    print(plants['fern'])

print(type(plants)) #class 'shelve.DbfilenameShelf

# Items can be continually added to the database. If a key exists, it will be
# overwritten. Print and delete the same way as with dicts:

with shelve.open('plants_shelf') as plants:
    plants['aloe'] = "healing gel inside"
    plants['jade'] = "round, waxy leaves"
    plants['fern'] = "full feathery leaves"
    plants['snake plant'] = "tall, seaweed like"

    del plants['yucca']                 # delete a key

    for key in plants:                  # print all the keys
        print(key)

    for value in plants.values():       # print all the values
        print(value)

    for item in plants.items():         # print both keys and values
        print(item)

    ordered_keys = list(plants.keys())  # print all the keys alphabetically
    ordered_keys.sort()
    for k in ordered_keys:
        print(k)


# Check for keys
# -----------------------------------------------------------------------------

plants = shelve.open('plants_shelf')
while True:
    plant_key = input('Enter a plant (q to quit): ').lower()
    if plant_key == 'q':
        break

    description = plants.get(plant_key, "There's no " + plant_key)
    print(description)

# previous two lines could also be done like this:
    # if plant_key in plants:
    #     description = plants[plant_key]
    #     print(description)
    # else:
    #     print("There's no: " + plant_key)

plants.close()


# Example of more complex values
# -----------------------------------------------------------------------------

import shelve

margarita = ['tomato', 'basil', 'mozzarella']
pesto = ['pesto', 'artichoke', 'olives']
prosciutto = ['prosciutto', 'arugula', 'parmesan']
italian = ['chorizo', 'red onion', 'pancetta']

with shelve.open('pizzas') as pizzas:
    pizzas['Margarita'] = margarita
    pizzas['Pesto'] = pesto
    pizzas['Prosciutto'] = prosciutto
    pizzas['Italian'] = italian


# Append to a shelved list
# -----------------------------------------------------------------------------
# Ideally we would say -  pizzas['Pesto'].append('garlic') but it doesn't work
# because the data is actually appended to a copy of the list in memory.
# Instead you would have to do:

with shelve.open('pizzas') as pizzas:
    temp_list = pizzas['Pesto']
    temp_list.append('garlic')
    pizzas['Pesto'] = temp_list
    print(pizzas['Pesto'])

# or use the 'writeback' parameter:

with shelve.open('pizzas', writeback=True) as pizzas:
    pizzas['Italian'].append('mushroom')
    print(pizzas['Italian'])

# When you use writeback, Python caches the object in memory and doesn't
# actually update the shelve database file until you close the shelve or use
# the sync method (sync is called automatically when the shelve is closed).
# Keep in mind if there's been a lot of changes, this writing can take quite a
# while. The upside of using writeback is simpler code, the downside is
# heavier memory usage. Regarding sync, it writes everything to the file, but
# also clears the memory cache.


# Reminder
# -----------------------------------------------------------------------------
# To reiterate, keys & values can only be added to shelves via individual
# assignments, not as dictionary literals. If you had a bunch of dictionaries
# in a variable it would normally look like this:

topics = {'plants' : {'succulents' : ['Blue star', 'Chinesis', 'Black Prince'],
                     'orchids' : ['Phaleanopsis', 'Cattleya', 'Paphiopedilum'],
                     'tropicals' : ['Spider', 'Mandevilla', 'Red Ginger']},

         'pizzas' : {'margarita' : ['tomato', 'basil', 'mozzarella'],
                     'pesto' : ['pesto', 'artichoke', 'olives'],
                     'prosciutto' : ['prosciutto', 'arugula', 'parmesan'],
                     'italian' : ['chorizo', 'red onion', 'pancetta']},

         'house' : {'kitchen' : ['appliances', 'cookware', 'cabinets'],
                    'bedroom' : ['bed', 'closet', 'shelves'],
                    'bathroom' : ['toilet', 'shower', 'sink']}}

# But for a shelve, you would add like this:

import shelve

topics = shelve.open('topics')

topics['plants'] = {'succulents' : ['Blue star', 'Chinesis', 'Black Prince'],
                    'orchids' : ['Phaleanopsis', 'Cattleya', 'Paphiopedilum'],
                    'tropicals' : ['Spider', 'Mandevilla', 'Red Ginger']}

topics['pizzas'] = {'margarita' : ['tomato', 'basil', 'mozzarella'],
                    'pesto' : ['pesto', 'artichoke', 'olives'],
                    'prosciutto' : ['prosciutto', 'arugula', 'parmesan'],
                    'italian' : ['chorizo', 'red onion', 'pancetta']}

topics['house'] = {'kitchen' : ['appliances', 'cookware', 'cabinets'],
                   'bedroom' : ['bed', 'closet', 'shelves'],
                   'bathroom' : ['toilet', 'shower', 'sink']}

print(topics['house']['bedroom'])
topics.close()

# This could be useful as you could have all your big data objects in one
# file... in this file, each one is written to a shelve (essentially
# initializing the shelves). Then, from your main program file you could just
# open it as above (topics = shelve.open('topics'), have access to the data...
# and close it at the end.


# When NOT to use shelve
# -----------------------------------------------------------------------------
# Keep in mind that since values are being pickled as they're stored and
# unpickled as they're read back in, if the values are really complex, this
# can affect performance of the program. In addition, different systems may
# use different underlying database technologies for storing the shelve. If the
# program is likely to move to another system and needs to take it's data with
# it, shelve may not be a good choice as it may not work properly on the new
# system.


# Summary
# -----------------------------------------------------------------------------
# Shelve is just a persistent dictionary. With a regular dictionary, you'd
# have to run the code to re-create it every time your program starts up.
# Writing the data to a shelve makes it immediately available when the program
# starts. Also, if you allow the users to make changes, those changes would be
# persisted to disk, and be available next time.
