'''Basic Webmaps with Folium'''

# https://folium.readthedocs.io/en/latest/

# Folium builds on the data wrangling strengths of Python and the mapping
# strengths of the Leaflet.js library. Manipulate your data in Python, then
# visualize it in on a Leaflet map via Folium.

import folium
import pandas

# -----------------------------------------------------------------------------
# Folium classes & methods
# -----------------------------------------------------------------------------
print(dir(folium))
# ['Circle', 'CircleMarker', 'ClickForMarker', 'ColorMap', 'CssLink',
# 'CustomIcon', 'Div', 'DivIcon', 'Element', 'FeatureGroup', 'Figure',
# 'FitBounds', 'GeoJson', 'Html', 'IFrame', 'Icon', 'JavascriptLink',
# 'LatLngPopup', 'LayerControl', 'LinearColormap', 'Link', 'MacroElement',
# 'Map', 'Marker', 'PolyLine', 'Popup', 'RegularPolygonMarker', 'StepColormap',
# 'TileLayer','TopoJson', 'Vega', 'VegaLite', 'WmsTileLayer', 'absolute_import',
# 'division', 'features', 'folium', 'map', 'print_function', 'utilities' ...]

# -----------------------------------------------------------------------------
# Basics
# -----------------------------------------------------------------------------
# print(help(folium.Map()))

# There are many, many parameters for this class. Note that the 'tiles'
# parameter represents the background image and automatically defaults to
# 'OpenStreetMap' but you can also choose:

# - "OpenStreetMap"
# - "Mapbox Bright" (Limited levels of zoom for free tiles)
# - "Mapbox Control Room" (Limited levels of zoom for free tiles)
# - "Stamen" (Terrain, Toner, and Watercolor)
# - "Cloudmade" (Must pass API key)
# - "Mapbox" (Must pass API key)
# - "CartoDB" (positron and dark_matter)

# print(help(folium.Icon))

# For folium.Icon() you can pass the following for the color of the marker:
#  ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred',
#   'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white',
#   'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']

# – icons can be found here: http://fontawesome.io/icons/
# – adding fa-inverse to the name of the icon allows it to be not black

loc = [[49.25, -123.115],
       [48.434, -123.354],
       [49.157, -120.916]]

# create a map object:
map_1 = folium.Map(location=loc[0],
                   detect_retina=True,
                   zoom_start=6,
                   tiles="CartoDB positron")

icon1 = folium.Icon(color='purple',
                   icon_color='orange',
                   icon='fa-heart fa-inverse',
                   prefix='fa')

icon2 = folium.Icon(color='green',
                   icon_color='darkgreen',
                   icon='fa-tree fa-inverse',
                   prefix='fa')

# BUG: If you try to apply the same icon variable to more than one marker,
# it doesn't work... only one marker will show.

# add markers this way:
# map_1.add_child(folium.Marker(location=loc[1], popup='Info', icon=icon1))
# map_1.add_child(folium.Marker(location=loc[2], popup='Info', icon=icon2))

# or this way (make more sense to me):
# folium.Marker(location=loc[1], popup='Info', icon=icon1).add_to(map_1)
# folium.Marker(location=loc[2], popup='Info', icon=icon2).add_to(map_1)

# add a 'FeatureGroup' - this lets you add a bunch of items as a group and
# works better with some of the layer control features:
fgv = folium.FeatureGroup(name='Volcanoes')
fgp = folium.FeatureGroup(name='Population')

# markers can then be added this way:
# folium.Marker(location=loc[1], popup='Info', icon=icon1).add_to(fgv)
# folium.Marker(location=loc[2], popup='Info', icon=icon2).add_to(fgv)

# -----------------------------------------------------------------------------
# Add Markers by iterating through data from a file
# -----------------------------------------------------------------------------

data = pandas.read_csv('data/volcanoes.csv')

latitudes = list(data['LAT'])
longitudes = list(data['LON'])
elevation = list(data['ELEV'])
name = list(data['NAME'])

def color_elev(elevation):
    '''return a different color for markers based on elevation'''
    if elevation < 1500:
        return 'pink'
    elif elevation < 2500:
        return 'purple'
    else:
        return 'darkpurple'

def hex_color_elev(elevation):
    '''return a different hex color for markers based on elevation'''
    if elevation < 1500:
        return '#f7a797'
    elif elevation < 2500:
        return '#fe6b6b'
    else:
        return '#8b1919'

# regular markers:
# print(help(folium.Marker))

# for lat, lon, e, n in zip(latitudes, longitudes, elevation, name):
#     folium.Marker(
#         location=[lat, lon],
#         popup=folium.Popup(str(n) + ' – elevation: ' + str(e) + ' m', parse_html=True),
#         icon=folium.Icon(color=color_by_elev(e), icon_color='white',
#         icon='fa-camera fa-inverse', prefix='fa')
#         ).add_to(fgv)

# circle markers:
# print(help(folium.CircleMarker))

for lat, lon, e, n in zip(latitudes, longitudes, elevation, name):
    folium.CircleMarker(
        location=[lat, lon],
        popup=folium.Popup(str(n) + ' – elevation: ' + str(e) + ' m', parse_html=True),
        radius=7,
        color=hex_color_elev(e),
        fill=True,
        fill_opacity=0.4,
        ).add_to(fgv)

# -----------------------------------------------------------------------------
# Add a polygon layer:
# -----------------------------------------------------------------------------

json_file = open('data/world.json', 'r', encoding='utf-8-sig').read()
json_style = lambda x: {
    'fillColor': 'green' if x['properties']['POP2005'] < 10000000
    else 'blue' if 10000000 <= x['properties']['POP2005'] < 20000000
    else 'orange'}

fgp.add_child(folium.GeoJson(data=json_file, style_function=json_style))

# -----------------------------------------------------------------------------
# Add final elements to the map and save:
# -----------------------------------------------------------------------------
# add the feature groups to the map:
map_1.add_child(fgv)
map_1.add_child(fgp)

# add the ability to click on any spot to see longitude and latitude:
map_1.add_child(folium.LatLngPopup())

# add ability to toggle layer visibility:
map_1.add_child(folium.LayerControl())

# save the map as an html file:
map_1.save('map1.html')
