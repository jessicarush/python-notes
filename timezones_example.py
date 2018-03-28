'''Timezones Example'''

# A program that allows a user to choose one time zones from a list.
# The program will then display the time in that timezone,
# as well as local time & UTC time.

import datetime
import pytz


# References
# -----------------------------------------------------------------------------
# print all timezones:
for x in pytz.all_timezones:
    print(x)

# print all country names, timezones and their times:
for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]))
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t{}: {}:".format(zone, local_time))
    else:
        print("\tNo timezone defined")


# Program
# -----------------------------------------------------------------------------

timezones = {'vancouver' : 'America/Vancouver',
             'luxembourg' : 'Europe/Luxembourg',
             'hong kong' : 'Hongkong',
             'switzerland' : 'Europe/Zurich',
             'shanghai' : 'Asia/Shanghai',
             'cuba' : 'America/Havana',
             'berlin' : 'Europe/Berlin',
             'turks & caicos' : 'America/Grand_Turk',
             'singapore' : 'Singapore'}

for zone in sorted(timezones):
    print(zone.title())

while True:
    selection = input('Choose a country (q to quit): ').lower()
    if selection == 'q':
        break
    if selection in timezones:
        country = timezones[selection]
        tz_to_display = pytz.timezone(country)
        world_time = datetime.datetime.now(tz=tz_to_display)

        # unformatted output:
        # print("{} time is: {}".format(selection.title(), world_time))
        # print("Local time is: {}".format(datetime.datetime.now()))
        # print("UTC is: {}".format(datetime.datetime.utcnow()))

        # fancier output:
        world = '{} time is:'.format(selection.title())
        local = 'Local time is:'
        utc = 'UTC time is:'
        print("{:24} {} {}".format(
              world, world_time.strftime('%A %x %X'), world_time.tzname()))
        print("{:24} {}".format(
              local, datetime.datetime.now().strftime('%A %x %X')))
        print("{:24} {}".format(
              utc, datetime.datetime.utcnow().strftime('%A %x %X')))
    else:
        print("That's not in my list")
