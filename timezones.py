'''Timezones'''

# A reminder: it's best to avoid working with timezones. Instead, the best
# practice would be to convert any times/dates to UTC at the start, do all
# your processing in UTC and then convert back to timezones only if you have
# to at the end for the user.

# As it turns out, the web browser knows the user's timezone, and exposes it
# through the standard date and time JavaScript APIs. A good way of utilizing
# this is to let the conversion from UTC to a local timezone happen in the
# web client using JavaScript. There is a small open-source JavaScript library
# called moment.js that handles this very well. Though not demonstrated in this
# file, note that there is a Flask extension called Flask-Moment that makes it
# easy to incorporate moment.js into your Flask app.


# pytz module
# -----------------------------------------------------------------------------

import pytz
import datetime

# FYI pytz pulls timezone information from this database:
# https://www.iana.org/time-zones

# see all timezone:

# for x in pytz.all_timezones:
#     print(x)
#
# # see all country codes:
#
# for x in sorted(pytz.country_names):
#     print(x, ':', pytz.country_names[x])
#
# # see all country names:
#
# for x in sorted(pytz.country_names):
#     print("{}: {}: {}".format(
#           x, pytz.country_names[x], pytz.country_timezones.get(x)))
#
# # see names, zones and their times:
#
# for x in sorted(pytz.country_names):
#     print("{}: {}".format(x, pytz.country_names[x]))
#     if x in pytz.country_timezones:
#         for zone in sorted(pytz.country_timezones[x]):
#             tz_to_display = pytz.timezone(zone)
#             local_time = datetime.datetime.now(tz=tz_to_display)
#             print("\t{}: {}:".format(zone, local_time))
#     else:
#         print("\tNo timezone defined")


# pytz example:
# -----------------------------------------------------------------------------

country = "Europe/Moscow"
tz_to_display = pytz.timezone(country)
world_time = datetime.datetime.now(tz=tz_to_display)

print("UTC is {}".format(datetime.datetime.utcnow()))
# The time in Europe/Moscow is 2017-11-24 01:40:00.944335+03:00

print("The time in {} is {}".format(country, world_time))
# The time in Europe/Moscow is 2017-11-24 01:40:00.944335+03:00

print("The time in {} is {} {}".format(
  country, world_time.strftime('%A %x %X'), world_time.tzname()))
# The time in Europe/Moscow is Friday 11/24/17 01:40:00 MSK


# convert a naive datetime to an aware datetime
# -----------------------------------------------------------------------------

import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time: {}".format(local_time))
print("Naive UTC: {}".format(utc_time))

# Naive local time: 2017-11-23 14:41:55.967259
# Naive UTC: 2017-11-23 22:41:55.967261

# when these next two print you can tell they are aware because they now
# include an offset at the end. Both will show the same time zone and same
# offset (+00:00, UTC) because the naive datetimes we supplied to it don't
# carry that information.

aware_local_time = pytz.utc.localize(local_time)
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time: {} - time zone: {}".format(
  aware_local_time, aware_local_time.tzinfo))

print("Aware UTC: {} - time zone: {}".format(
  aware_utc_time, aware_utc_time.tzinfo))

# Try this instead to show the correct local offset and time zone:

aware_local_time = pytz.utc.localize(utc_time).astimezone()

print("Aware local time: {} - time zone: {}".format(
  aware_local_time, aware_local_time.tzinfo))

# Aware local time: 2017-11-23 14:41:55.967259+00:00 - time zone: UTC
# Aware UTC: 2017-11-23 22:41:55.967261+00:00 - time zone: UTC
# Aware local time: 2017-11-23 14:41:55.967261-08:00 - time zone: PST


# date in a timezone from epoch
# -----------------------------------------------------------------------------
# Use time stamps (seconds since the epoch) to convert to actual date.
# For this example we'll be supplying the time zone since an epoch number could
# be from anywhere. This particular timestamp is the hour before DST in the UK
# on October 25, 2015. You will see the difference before and after the DST in
# the offset.

s = 1445733000
t = s +(60 * 60)

gb = pytz.timezone("GB")
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print('{} seconds since epoch is {}'.format(s, dt1))
print('{} seconds since epoch is {}'.format(t, dt2))

# 1445733000 seconds since epoch is 2015-10-25 01:30:00+01:00
# 1445736600 seconds since epoch is 2015-10-25 01:30:00+00:00
