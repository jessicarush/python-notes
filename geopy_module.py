'''A Brief look at Geopy'''

# geopy is a Python client for several popular geocoding web services. geopy
# makes it easy to locate the coordinates of addresses, cities, countries, and
# landmarks across the globe using third-party geocoders and other data sources.

# geopy includes geocoder classes for the OpenStreetMap Nominatim, ESRI ArcGIS,
# Google Geocoding API (V3), Baidu Maps, Bing Maps API, Yahoo! PlaceFinder,
# Yandex, IGN France, GeoNames, NaviData, OpenMapQuest, What3Words, OpenCage,
# SmartyStreets, geocoder.us, and GeocodeFarm geocoder services. The various
# geocoder classes are located in geopy.geocoders.

# $ pip3 install geopy

from geopy.geocoders import GoogleV3


geolocator = GoogleV3(scheme='http')

address1 = '3995 23rd St, San Francisco, CA 94114, USA'
address2 = '3730 Cambie St, Vancouver, BC V5Z2X5, Canada'

location = geolocator.geocode(address2)

print(type(location))    # <class 'geopy.location.Location'>
print(location)          # 3995 23rd St, San Francisco, CA 94114, USA
print(location.address)  # 3995 23rd St, San Francisco, CA 94114, USA
print((location.latitude, location.longitude))
# (37.7529353, -122.4317224)
