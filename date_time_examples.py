'''datetime Examples'''

# Compare usages -----------------------------------------------------------------

import datetime
import pytz

now = datetime.datetime.now()
# 2017-10-02 16:03:01.558993 <class 'datetime.datetime'>

utc = datetime.datetime.utcnow()
# 2017-10-02 23:03:01.559071 <class 'datetime.datetime'>

the_time = pytz.utc.localize(datetime.datetime.utcnow())
# 2017-10-02 23:03:01.559084+00:00 <class 'datetime.datetime'>

the_local_time = the_time.astimezone()
# 2017-10-02 16:03:01.559084-07:00 <class 'datetime.datetime'>

the_local_time = pytz.utc.localize(datetime.datetime.utcnow()).astimezone()
# 2017-10-02 16:03:01.559084-07:00 <class 'datetime.datetime'>

timezone = the_local_time.tzinfo
# PDT <class 'datetime.timezone'>

timestamp = datetime.datetime.now().strftime('%a %x')
# Mon 10/02/17 <class 'str'>

backdated = datetime.date(2017, 8, 7).strftime('%a %x')
# Mon 08/07/17 <class 'str'>



# timedelta example ------------------------------------------------------------

# What dates do I need to water the plants if the watering schedule is:
# – every 4 days in summer - summer is 3 more weeks from today
# – every 6 days in fall - fall is 14 weeks following summer
# – every 8 days in winter - winter is 14 weeks following fall

from datetime import date
from datetime import timedelta

now = date.today()

freq_summer = 4
freq_fall = 6
freq_winter = 8

count_summer = ((7*3) // freq_summer)
count_fall = ((7*14) // freq_fall)
count_winter = ((7*14) // freq_winter)

freq_summer = timedelta(days = freq_summer)
freq_fall = timedelta(days = freq_fall)
freq_winter = timedelta(days = freq_winter)

print('summer water schedule:')

for num in range(1, count_summer+1):
    print(now + (num * freq_summer))

print('fall water schedule:')

end_of_summer = now + (count_summer * freq_summer)

for num in range(1, count_fall+1):
    print(end_of_summer + (num * freq_fall))

print('winter water schedule:')

end_of_fall = end_of_summer + (count_fall * freq_fall)

for num in range(1, count_winter+1):
    print(end_of_fall+ (num * freq_winter))
