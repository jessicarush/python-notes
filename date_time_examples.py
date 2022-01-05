'''datetime Examples'''


# Compare usages
# -----------------------------------------------------------------------------

import datetime
import pytz

now = datetime.datetime.now()
# 2017-10-02 16:03:01.558993  <class 'datetime.datetime'>

utc = datetime.datetime.utcnow()
# 2017-10-02 23:03:01.559071  <class 'datetime.datetime'>

the_time = pytz.utc.localize(datetime.datetime.utcnow())
# 2017-10-02 23:03:01.559084+00:00  <class 'datetime.datetime'>

the_local_time = the_time.astimezone()
# 2017-10-02 16:03:01.559084-07:00  <class 'datetime.datetime'>

the_local_time = pytz.utc.localize(datetime.datetime.utcnow()).astimezone()
# 2017-10-02 16:03:01.559084-07:00  <class 'datetime.datetime'>

timezone = the_local_time.tzinfo
# PDT <class 'datetime.timezone'>

formatted = datetime.datetime.now().strftime('%m-%d-%Y, %H:%M %p')
# 12-31-2017, 10:47 AM  <class 'str'>

timestamp = datetime.datetime.now().strftime('%a %x')
# Mon 10/02/17  <class 'str'>

backdated = datetime.date(2017, 8, 7).strftime('%a %x')
# Mon 08/07/17  <class 'str'>

print(f'{now.month}/{now.day}/{now.year}')
# 1/5/2022


# timedelta example
# -----------------------------------------------------------------------------
# The following function will output a plant watering schedule using the
# datetime timedelta method.

from datetime import date
from datetime import timedelta

def watering_schedule(x):
    '''Calculate a plant watering schedule for the next 'x' waterings'''
    # categorize each month into seasons:
    winter_months = [1, 2, 3, 12]
    summer_months = [6, 7, 8, 9]
    # watering frequency every n days:
    winter_freq = 6
    spring_fall_freq = 5
    summer_freq = 4
    # check the month and generate schedule:
    now = date.today()
    schedule = []
    while len(schedule) < x:
        if now.month in summer_months:
            now += timedelta(days=summer_freq)
            schedule.append(now)
        elif now.month in winter_months:
            now += timedelta(days=winter_freq)
            schedule.append(now)
        else:
            now += timedelta(days=spring_fall_freq)
            schedule.append(now)
    print('Watering Schedule:')
    for i in schedule:
        print(i)

watering_schedule(25)
