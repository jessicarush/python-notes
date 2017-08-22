# What dates do I need to water the plants if watering schedule is:
# every 4 days in summer - summer is 3 more weeks from today
# every 6 days in fall - fall is 3 months following summer
# every 8 days in winter - winter is 3 months following fall

from datetime import date
from datetime import timedelta

now = date.today()

freq_summer = 4
freq_fall = 6
freq_winter = 8

count_summer = ((7*3) // freq_summer)
count_fall = ((7*13) // freq_fall)
count_winter = ((7*13) // freq_winter)

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
