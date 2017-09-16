'''Timezones'''

# As discussed, it's best to avoid working with timezones. Instead, the best
# practice would be to convert any times/dates to UTC at the start, do all
# your processing in UTC and then convert back to timezones only if you have
# to at the end for the user.

# pytz module ----------------------------------------------------------------

import pytz
import datetime

# FYI pytz pulls timezone information from this database:
# https://www.iana.org/time-zones

# see all timezone:

for x in pytz.all_timezones:
    print(x)

# see all country codes:

for x in sorted(pytz.country_names):
    print(x, ':', pytz.country_names[x])

# see all counrty names:

for x in sorted(pytz.country_names):
    print("{}: {}: {}".format(
          x, pytz.country_names[x], pytz.country_timezones.get(x)))

# see names, zones and their times:

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]))
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t{}: {}:".format(zone, local_time))
    else:
        print("\tNo timezone defined")

# example:

country = "Europe/Moscow"
tz_to_display = pytz.timezone(country)
world_time = datetime.datetime.now(tz=tz_to_display)

print("The time in {} is {}".format(country, world_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

# fancier:
print("The time in {} is {} {}".format(
country, world_time.strftime('%A %x %X'), world_time.tzname()))

# convert a naive datatime to an aware datetime ------------------------------

import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time: {}".format(local_time))
print("Naive UTC: {}".format(utc_time))

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

# date in a time zone from epoch ---------------------------------------------

# Using time stamps (seconds since the epoch) to convert to actual date.
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
