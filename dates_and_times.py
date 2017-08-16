# Calendars & Clocks

# Working with dates and times can be a bit of a pain on account of varying
# formats, time zones, daylight savings times, and so on.

# Python’s standard library has many date and time modules: datetime, time,
# calendar, dateutil, and others. There’s some overlap, and it’s a bit
# confusing.

# Example: test if a year is a leap year:

import calendar

print(calendar.isleap(2016))
print(calendar.isleap(2017))

# The datetime module defines four main objects... each with many methods:

# date - for years, months, days
# time - for hours, minutes, seconds, and fractions
# datetime - for dates and times together
# timedelta - for date and/or time intervals

# make a date object by specifying a year, month, and day. Those values are
# then available as attributes:

from datetime import date

halloween = date(2017, 10, 31)
print(halloween.day)
print(halloween.month)
print(halloween.year)

# print a date with isoformat() method:

print(halloween.isoformat())

# The iso refers to ISO 8601, an international standard for representing dates
# and times. It goes from most general (year) to most specific (day). It also
# sorts correctly: by year, then month, then day.

# today() method to generate today’s date:

from datetime import date
now = date.today()
print(now)

# This makes use of a timedelta object to add a time interval to a date:

from datetime import timedelta

one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)
print(now + 18*one_day)

# See also: timedelta_example.py

# Note: The range of date is from date.min (year=1, month=1, day=1) to
# date.max (year=9999, month=12, day=31). As a result, you can’t use it for
# historic or astronomical calculations.

# The datetime module’s time object is used to represent a time of day:

from datetime import time

noon = time(12, 0, 1)

print(noon.hour)
print(noon.minute)
print(noon.second)
print(noon.microsecond)

# The arguments go from the largest time unit (hours) to the smallest
# (microseconds). If you don’t provide all the arguments, time assumes all the
# rest are zero.

# The datetime object includes both the date and time of day. The following
# would be for August 16, 2017, at 2:09 P.M., plus 5 seconds, 6 microseconds:

from datetime import datetime

a_day = datetime(2017, 8, 16, 14, 9, 5, 6)

# The datetime object also has an isoformat() method:

print(a_day.isoformat())

# datetime has a now() method with which you can get the current date and time:

now = datetime.now()
print(now.isoformat())
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

# You can merge a date object and a time object into a datetime object by
# using combine():

from datetime import datetime, time, date

noonish = time(12, 3, 0)
this_day = date.today()
noonish_today = datetime.combine(this_day, noonish)

print(noonish_today)
print(type(noonish_today))

# You can pull the date and time out from a datetime by using the date() and
# time() methods:

print(noonish_today.date())
print(noonish_today.time())

# Time Module

# It is confusing that Python has a datetime module with a time object, and a
# separate time module. Furthermore, the time module has a function called...
# time().

# One way to represent an absolute time is to count the number of seconds
# since some starting point. Unix time uses the number of seconds since
# midnight on January 1, 1970. This value is called the epoch. Epoch values
# are a useful least-common denominator for date and time exchange with
# different systems, such as JavaScript.

# The time module’s time() function returns the current time as an epoch
# value (number of seconds since 1970-01-01):

import time
now = time.time()
print(now)

# convert an epoch value to a string by using ctime():

new_now = time.ctime(now)
print(new_now)
print(type(new_now)) # it's a string

# Sometimes, though, you need actual days, hours, and so on, which time provides 
# as struct_time objects. localtime() provides the time in your system’s time zone, 
# and gmtime() provides it in UTC.

# Note: UTC is the time standard commonly used across the world. It is not a
# time zone but a time standard that is the basis for civil time and time
# zones worldwide. This means that no country or territory officially uses
# UTC as a local time. Formerly GMT (Greenwich Mean Time) which is now a time zone.

print(time.localtime(now))
print(time.gmtime(now))
type(time.localtime(now)) # <class 'time.struct_time'>

# The opposite of these is mktime(), which converts a struct_time object to
# epoch seconds:

tm = time.localtime(now)
print(time.mktime(tm))

# Note this doesn’t exactly match the earlier epoch value of now() because
# the struct_time object preserves time only to the second.

# Some advice: wherever possible, use UTC instead of time zones. UTC is an
# absolute time, independent of time zones. If you have a server, set its
# time to UTC; do not use local time.

# Also, if possible, avoid the use of daylight savings time.

# Read and Write Dates & Times

# isoformat() for date, time and datetime objects and, ctime() for epochs
# aren't the only way to write dates and times. We can also convert dates,
# times to strings using strftime().

# This is provided as a method in the datetime, date, and time objects, and
# as a function in the time module. strftime() uses format strings to specify
# the output:

# %Y  year                    2017
# %m  month                   08
# %B  month name              August
# %b  month abbreviation      Aug
# %d  day of month            16
# %A  weekday name            Wednesday
# %a  weekday abbreviation    Wed
# %H  hour (24 hr)            15
# %I  hour (12 hr)            03
# %p  AM/PM                   PM
# %M  minute                  59
# %S  second                  59

# Here’s the strftime() function with the time module. It converts a
# struct_time object to a string:

import time

fmt = "It's %A, %B %d, %Y, local time: %I:%M:%S%p"

t = time.localtime()

# Emphasis: for this method Tuple or struct_time argument required at 't':

print(time.strftime(fmt, t))

# If we try with a date object, the time defaults to midnight:

a_day = date(2017, 8, 16)
print(a_day.strftime(fmt))

# If we try with a time object, we get a default date of 1900-01-01

# have to import again otherwise it will try to use time from import time
from datetime import time

a_time = time(12, 3, 0)
print(a_time.strftime(fmt))

# To go the other way and convert a string to a date or time, use strptime()
# the nonformat parts of the string (without %) need to match EXACTLY.
# Example: specify a format that matches year-month-day, such as 2017-08-16.

import time

fmt = '%Y-%m-%d'
a_date = time.strptime('2017-08-16', fmt)
print(a_date)

# Note: Names are specific to your locale (internationalization settings for
# your os). To print different month and day names, change your locale by
# using setlocale(). Its first argument is locale.LC_TIME for dates and
# times, and the second is a string combining the language and country
# abbreviation:

import locale
from datetime import date

halloween = date(2017, 10, 31)

for lang_country in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is',]:
    locale.setlocale(locale.LC_TIME, lang_country)
    print(halloween.strftime('%A, %B %d'))

# The above does english, french, german, spanish, icelandic. For a complete
# list of lang_country...

import locale
names = locale.locale_alias.keys()

# not all the names work with setlocale(). The ones we're looking for are a
# two character language code followed by '_' and two character country code:

useable_names = [name for name in names if len(name) == 5 and name[2] == '_']
print(useable_names)

# if you wanted all the german names:

de_names = [name for name in useable_names if name.startswith('de')]
print(de_names)

# language codes - https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
# country codes - https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

# Alternative Modules

# If you find the standard library modules confusing, or lacking a particular 
# conversion that you want, there are many third-party alternatives:

# arrow - https://arrow.readthedocs.io/en/latest/
# This combines many date and time functions with a simple API.

# dateutil - http://labix.org/python-dateutil
# This module parses almost any date format and handles relative dates and 
# times well.

# iso8601 - https://pypi.python.org/pypi/iso8601
# This fills in gaps in the standard library for the ISO8601 format.

# fleming - https://github.com/ambitioninc/fleming
# This module offers many time zone functions.
