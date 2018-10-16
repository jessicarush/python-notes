'''Pygal - Mapping Global Data Sets: JSON format'''


# The data in this example comes from:
# http://data.okfn.org/

import json
import pygal
from pygal.maps.world import COUNTRIES
from pygal.maps.world import World
from pygal.style import Style


# Explore/Analyze the data
# -----------------------------------------------------------------------------

# load the data into a list:
filename = 'data/population_data.json'
with open(filename) as fob:
    pop_data = json.load(fob)

# print one year for each country:
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # some of the populations strings have decimals. In order to
        # convert them all to ints, we need to convert to floats first.
        population = int(float(pop_dict['Value']))
        print(country_name, '–', population)


# Extract the data
# -----------------------------------------------------------------------------
# To use pygals mapping tools, countries need to be provided as country codes.
# Pygals country codes are stored in a module called pygal_maps_world is a
# dictionary called COUNTRIES. You have to do a separate pip install for this:
# $ pip3 install pygal_maps_world. Then: pygal.maps.world import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])

def get_country_code(country_name):
    '''Return the Pygal 2-digit country code for a given country.'''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # if the name isn't found, return None:
    return None

# Test it out:
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        else:
            print('Error –', country_name)

# There are a quite a few Errors (obv) which fall mainly into two categories:
#    – some country names don't match exactly (ie Yemen, Rep vs Yemen)
#    – some lines in the dataset aren't by country at all but by region
#      (ie Arab World) or by economic group (ie all income levels).

# For the moment, we'll just plot the stuff that matched.


# Plot the data
# -----------------------------------------------------------------------------
# group the countries into 3 population levels to have the colouring be more
# informative (otherwise it just shows China and India a contrastig colour).

cc_pop1, cc_pop2, cc_pop3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:      # 10 million
        cc_pop1[cc] = pop
    elif pop < 1000000000:  # 1 billion
        cc_pop2[cc] = pop
    else:
        cc_pop3[cc] = pop

# see how many countries are in each group:
print(len(cc_pop1), len(cc_pop2), len(cc_pop3))

my_style = Style(
    legend_font_size=9,
    colors=('#509aff', '#01e7d4', '#ff6e67'))

wm = World(style=my_style)
wm.title = 'World Population in 2010'

# wm.add('North America',['ca', 'mx', 'us'])
# wm.add('North America',{'ca': 34126000, 'mx': 113423000, 'us': 309349000})
# wm.add('2010', cc_populations)

wm.add('0-10m', cc_pop1)
wm.add('10m-1b', cc_pop2)
wm.add('>1b', cc_pop3)

wm.render_to_file('americas.svg')
