'''Matplotlib – Weather Data'''

# The weather data for this example was originally obtained from:
# https://www.wunderground.com/history/
# Some other good data sources for historical weather data:
# https://www.ncdc.noaa.gov/data-access/quick-links
# http://climate.weather.gc.ca/index_e.html

import csv
from datetime import datetime
from matplotlib import pyplot as plt


filename = 'data/death_valley_2014.csv'
placename = 'Death Valley, CA'


# Exploring the data:
# -----------------------------------------------------------------------------

with open(filename) as fob:
    reader = csv.reader(fob)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)


# Extracting and reading data:
# -----------------------------------------------------------------------------

with open(filename) as fob:
    reader = csv.reader(fob)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# Plotting the data:
# -----------------------------------------------------------------------------

# creates a figure and one subplot
fig, ax = plt.subplots(figsize=(10, 5))

# plot the data:
plt.plot(dates, highs, c='tomato', alpha=0.6)
plt.plot(dates, lows, c='darkturquoise', alpha=0.6)

# format the plot:
plt.fill_between(dates, highs, lows, facecolor='gold', alpha=0.2)
title = 'Daily high and low temperatures, 2014\n{}'.format(placename)
plt.title(title, fontsize=10)
plt.xlabel('', fontsize=9)
fig.autofmt_xdate()
plt.xticks(rotation=25)
plt.ylabel('Termperature (F)', fontsize=9, fontweight='bold')
plt.tick_params(axis='both', which='major', labelsize=7)

# tells x, y axis to use this range
# plt.axis([datetime(2014, 1, 1), datetime(2014, 12, 1), 0, 120])
# if you just want to set one axis:
ax.set_xlim([datetime(2014, 1, 1), datetime(2014, 12, 1)])
# ax.set_ylim([20, 120])

# display the plot:
plt.show()
