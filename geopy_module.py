'''A Brief look at Geopy'''


# https://geopy.readthedocs.io/en/stable/

# geopy is a Python client for several popular geocoding web services. geopy
# makes it easy to locate the coordinates of addresses, cities, countries, and
# landmarks across the globe using third-party geocoders and other data sources.

# geopy includes geocoder classes for: ArcGIS, AzureMaps, Baidu, BANFrance,
# Bing, DataBC, GeocodeEarth, GeocodeFarm, Geolake, GeoNames, GoogleV3, HERE,
# IGNFrance, MapBox, OpenCage, OpenMapQuest, Nominatim, Pelias, Photon,
# PickPoint, LiveAddress, TomTom, What3Words, Yandex. The majority of these
# require a (not free) API key or usernamename/password paramter. The various
# geocoder classes are located in geopy.geocoders.

# As of July 2018 Google requires each request to have a paid API key.
# https://developers.google.com/maps/documentation/geocoding/usage-and-billing

# $ pip3 install geopy

# from geopy.geocoders import GoogleV3
# from geopy.geocoders import Yandex
# from geopy.geocoders import DataBC
from geopy.geocoders import Photon

# geolocator = GoogleV3(scheme='http')
# geolocator = Yandex(lang='en', scheme='http')
# geolocator = DataBC(scheme='http')
geolocator = Photon(scheme='http')


address1 = '3995 23rd St, San Francisco, CA 94114, USA'
address2 = '3730 Cambie St, Vancouver, BC V5Z2X5, Canada'

location = geolocator.geocode(address1)

print(type(location))
# <class 'geopy.location.Location'>
print(dir(location))
# [... 'address', 'altitude', 'latitude', 'longitude', 'point', 'raw']
print(location)
# 3995 23rd St, San Francisco, CA 94114, USA
print(location.address)
# 3995 23rd St, San Francisco, CA 94114, USA
print(location.altitude)
# 0.0
print((location.latitude, location.longitude))
# (37.7529648, -122.4317141)
print(location.point)
# 37 45m 10.6733s N, 122 25m 54.1708s W
print(location.raw)
# {'address_components': [
#     {'long_name': '3995', 'short_name': '3995', 'types': ['street_number']},
#     {'long_name': '23rd Street', 'short_name': '23rd St', 'types': ['route']},
#     {'long_name': 'Noe Valley', 'short_name': 'Noe Valley', 'types':
#       ['neighborhood', 'political']},
#     {'long_name': 'San Francisco', 'short_name': 'SF', 'types':
#       ['locality', 'political']},
#     {'long_name': 'San Francisco County', 'short_name': 'San Francisco County',
#       'types': ['administrative_area_level_2', 'political']},
#     {'long_name': 'California', 'short_name': 'CA', 'types':
#       ['administrative_area_level_1', 'political']},
#     {'long_name': 'United States', 'short_name': 'US', 'types':
#       ['country', 'political']},
#     {'long_name': '94114', 'short_name': '94114', 'types': ['postal_code']},
#     {'long_name': '3302', 'short_name': '3302', 'types': ['postal_code_suffix']}],
#  'formatted_address': '3995 23rd St, San Francisco, CA 94114, USA',
#  'geometry': {
#      'location': {'lat': 37.7529353, 'lng': -122.4317224},
#      'location_type': 'ROOFTOP',
#      'viewport': {
#          'northeast': {'lat': 37.75428428029149, 'lng': -122.4303734197085},
#          'southwest': {'lat': 37.75158631970849, 'lng': -122.4330713802915}}},
#  'place_id': 'ChIJp4irxxN-j4ARlJs-6IsSQGk', 'types': ['street_address']}
