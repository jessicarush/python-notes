'''Calendars & Clocks'''


# Working with dates and times can be a bit of a pain on account of varying
# formats, time zones, daylight savings times, and so on. Python's standard
# library has many date and time modules: datetime, time, calendar, locale
# and others. There's some overlap, and is a bit confusing:

# calendar module:
#   General calendar-related functions. It focuses on printing full clalendars
#   in various formats.

# datetime module:
#   Object-oriented interface to dates and times with similar functionality
#   to the time module.

# time module:
#   Low-level time related functions (time access and conversions)

# locale module:
#   Internationalization services. The locale setting affects the
#   interpretation of many format specifiers in strftime() and strptime().

# see also:
# https://pythontic.com/modules/datetime/introduction


# calendar module
# -----------------------------------------------------------------------------

import calendar

# Print a month as lists of dates (the first index[0] defaluts to Monday):
print(calendar.monthcalendar(2018, 11))
# [[0, 0, 0, 1, 2, 3, 4],
#  [5, 6, 7, 8, 9, 10, 11],
#  [12, 13, 14, 15, 16, 17, 18],
#  [19, 20, 21, 22, 23, 24, 25],
#  [26, 27, 28, 29, 30, 0, 0]]

# Test if a year is a leap year:
print(calendar.isleap(2016))  # True
print(calendar.isleap(2017))  # False

# The TextCalendar and HTMLCalendar classes can produce preformatted output:
c = calendar.TextCalendar(calendar.MONDAY)

# The prmonth() method prints the formatted text output for a given month:
c.prmonth(1974, 11)

#   November 1974
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30

# The HTMLCalendar class and formatmonth() method output an HTML table:
c = calendar.HTMLCalendar(calendar.MONDAY)
print(c.formatmonth(1974, 11))

# <table border="0" cellpadding="0" cellspacing="0" class="month">
# <tr><th colspan="7" class="month">November 1974</th></tr>
# <tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th>
# ... etc ...


# datetime module overview
# -----------------------------------------------------------------------------
# The datetime module defines four main objects, each with many methods:
# – datetime.date() for years, months, days
# – datetime.time() for hours, minutes, seconds, and fractions
# – datetime.datetime() for dates and times together
# – datetime.timedelta() for date and/or time intervals

# Note with datetime objects, some are considered naive and some are aware.
# Aware objects are aware of the timezone offset and naive objects are not.


# datetime.date()
# -----------------------------------------------------------------------------

from datetime import date

# Use the today() method to generate today's date:

now = date.today()

print(now)  # 2017-11-07

# Make a date() object by passing a year, month, and day:

future = date(2024, 11, 9)

# Those values are then available as attributes:

print(future.day)    # 9
print(future.month)  # 11
print(future.year)   # 2024

# Print a date with isoformat() method:

print(future.isoformat())  # 2024-11-09

# isocalendar() returns a tuple of the year, week number and weekday number:

print(future.isocalendar())  # (2024, 45, 6)

# isoweekday() returns the weekday from above where 1=Monday, 7=Sunday

print(future.isoweekday())  # 6

# The iso refers to ISO 8601, an international standard for representing dates
# and times. It goes from most general (year) to most specific (day). It also
# sorts correctly: by year, then month, then day.

# The weekday() method works the same as isoweekday except 0=Monday, 6=Sunday

print(future.weekday())  # 5

# fromisoformat() lets you convert an isoformat string into a date object:

date_from_iso = date.fromisoformat('2024-11-09')

print(date_from_iso.month)  # 11

# fromtimestamp() lets you convert a timestamp into a date object:

date_from_timestamp = date.fromtimestamp(1731139200)

print(date_from_timestamp.month)  # 11

# NOTE: you cannot create a timestamp from a date object or a time object,
# only a datetime object has a timestamp() method! For example:
# t = datetime(2024, 11, 9).timestamp()

# As of Python 3.8, you can also create a date object from isocalendar:

date_from_isocalendar = date.fromisocalendar(2024, 45, 6)

print(date_from_isocalendar.month)  # 11


# datetime.time()
# -----------------------------------------------------------------------------

from datetime import time

# The datetime module's time() object is used to represent a time of day:

noon = time(12, 0, 1)

print(noon.hour)         # 12
print(noon.minute)       # 0
print(noon.second)       # 1
print(noon.microsecond)  # 0

# The arguments go from the largest time unit (hours) to the smallest
# (microseconds). If you don't provide all the arguments, time assumes all the
# rest are zero.


# datetime.datetime()
# -----------------------------------------------------------------------------

from datetime import datetime

# The datetime() object includes both the date and time of day. The following
# would be for August 16, 2017, at 2:09 P.M., plus 5 seconds, 6 microseconds:

a_day = datetime(2017, 8, 16, 14, 9, 5, 6)

# Note that if you skip the time, it will be midnight:

print(datetime(2024, 11, 9))  # 2024-11-09 00:00:00

# The datetime object also has an isoformat() method:

print(a_day.isoformat())  # 2017-08-16T14:09:05.000006

# As with date(), the isocalendar() method returns the week and weekday:

print(a_day.isocalendar())  # (2017, 33, 3)

# The datetime object has a timestamp() method:

print(a_day.timestamp())  # 1502917745.000006

# You can covert back to a datetime from isoformat, isocalendar and timestamp:

date_from_iso = datetime.fromisoformat("2017-08-16T14:09:05")
date_from_isocalendar = datetime.fromisocalendar(2017, 33, 3)
date_from_timestamp = datetime.fromtimestamp(1502917745)

print(date_from_iso)          # 2017-08-16 14:09:05
print(date_from_isocalendar)  # 2017-08-16 00:00:00
print(date_from_timestamp)    # 2017-08-16 14:09:05

# datetime has methods that return the current date and time, local and utc:

print(datetime.today())   # 2017-11-07 16:17:15.343399
print(datetime.now())     # 2017-11-07 16:17:15.343410
print(datetime.utcnow())  # 2017-11-08 00:17:15.343416

# now() and today() are similar but now() allows us to provide timezone info
# with a tzinfo object (see timezones.py)

now = datetime.now()

print(now.isoformat())    # 2020-01-24T12:52:39.572236
print(now.isocalendar())  # (2020, 4, 5)
print(now.timestamp())    # 1579899159.572236
print(now.weekday())      # 4 (Monday=0, Sunday=6)
print(now.isoweekday())   # 5 (Monday=1, Sunday=7)
print(now.year)           # 2020
print(now.month)          # 1
print(now.day)            # 24
print(now.hour)           # 12
print(now.minute)         # 54
print(now.second)         # 39
print(now.microsecond)    # 572236

# You can merge a date object and a time object into a datetime object by
# using combine():

from datetime import datetime, time, date

noonish = time(12, 3, 0)
this_day = date.today()
noonish_today = datetime.combine(this_day, noonish)

print(noonish_today)        # 2017-11-07 12:03:00
print(type(noonish_today))  # <class 'datetime.datetime'>

# You can pull the date and time out from a datetime object by using the
# date() and time() methods:

print(noonish_today.date())  # 2017-11-07
print(noonish_today.time())  # 12:03:00


# datetime.timedelta()
# -----------------------------------------------------------------------------

from datetime import timedelta

# The timedelta() object can be used to add/subtract a time interval to a date,
# time or datetime object. You can pass in any of the following intervals:
# days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0

now = date.today()
one_week = timedelta(days=7)
five_years = timedelta(weeks=52)
minute_and_a_half = timedelta(minutes=1, seconds=30)

print(now + one_week)               # 2020-01-31
print(now + five_years)             # 2021-01-22
print(now + five_years - one_week)  # 2021-01-15

# subtracting two dates, datetimes or times will give you a timedelta object.
# Note that for this, the two operands must be the same type, i.e. you cannot
# subtract a datetime object from a date object.

future = date(2025, 1, 1)

time_diff = future - now

print(time_diff)        # 1804 days, 0:00:00
print(type(time_diff))  # <class 'datetime.timedelta'>

# Note: The range of date is from date.min (year=1, month=1, day=1) to
# date.max (year=9999, month=12, day=31). As a result, you can't use it for
# historic or astronomical calculations.

# See also: timedelta_example.py


# Time module
# -----------------------------------------------------------------------------

import time

# It is confusing that Python has a datetime module with a time object, and a
# separate time module. Furthermore, the time module has a function called...
# time().

# One way to represent an absolute time is to count the number of seconds
# since some starting point. Unix time uses the number of seconds since
# midnight on January 1, 1970. This value is called the epoch. Epoch values
# are a useful least-common denominator for date and time exchange with
# different systems, such as JavaScript.

# The time module's time() function returns the current time as an epoch
# value (number of seconds since 1970-01-01):

now = time.time()

print(now)                # 1510100475.260867
print(type(now))          # <class 'float'>

# convert an epoch value to a string by using ctime():

str_now = time.ctime(now)

print(str_now)            # Tue Nov  7 16:21:15 2017
print(type(str_now))      # <class 'str'>

test_time = time.ctime()  # if no arg is provided, the current time is used

print(test_time)          # Tue Nov  7 16:21:15 2017

# Sometimes, though, you need actual days, hours, and so on, which time
# provides as struct_time objects. localtime() provides the time in your
# system's time zone, and gmtime() provides it in UTC.

# Note: UTC is the time standard commonly used across the world. It is not a
# time zone but a time standard that is the basis for civil time and time
# zones worldwide. This means that no country or territory officially uses
# UTC as a local time. Formerly GMT (Greenwich Mean Time - is now a time zone).

print(time.localtime(now))
# time.struct_time(tm_year=2017, tm_mon=11, tm_mday=7, tm_hour=16, tm_min=23,
# tm_sec=56, tm_wday=1, tm_yday=311, tm_isdst=0)

print(time.localtime())
# time.struct_time(tm_year=2017, tm_mon=11, tm_mday=7, tm_hour=16, tm_min=23,
# tm_sec=56, tm_wday=1, tm_yday=311, tm_isdst=0)

print(time.gmtime(now))
# time.struct_time(tm_year=2017, tm_mon=11, tm_mday=8, tm_hour=0, tm_min=23,
# tm_sec=56, tm_wday=2, tm_yday=312, tm_isdst=0)

print(time.gmtime())
# time.struct_time(tm_year=2017, tm_mon=11, tm_mday=8, tm_hour=0, tm_min=23,
# tm_sec=56, tm_wday=2, tm_yday=312, tm_isdst=0)

print(type(time.localtime(now))) # <class 'time.struct_time'>

t = time.localtime()

print(f'Year {t.tm_year}, Month {t.tm_mon}, Day {t.tm_mday},'
      f'Hour {t.tm_hour}, Minute {t.tm_min}, Second {t.tm_sec},'
      f'Weekday {t.tm_wday}, Yearday {t.tm_yday}, DST {t.tm_isdst}')
# Year 2017, Month 11, Day 7, Hour 16, Minute 28, Second 23, Weekday 1,
# Yearday 311, DST 0

# mktime() converts the above struct_time objects back to epoch seconds:

tm = time.localtime(now)
tme = time.mktime(tm)

print(type(tm))   # <class 'time.struct_time'>
print(type(tme))  # <class 'float'>

# Note this doesn't exactly match the earlier epoch value of now() because
# the struct_time object preserves time only to the second.

# Some advice: wherever possible, use UTC instead of time zones. UTC is an
# absolute time, independent of time zones. If you have a server, set its
# time to UTC; do not use local time.

# Also, if possible, avoid the use of daylight savings time. That being said:


# Timezones and DST (see also timezones.py)
# -----------------------------------------------------------------------------

import time

# time.tzname[]:
# A tuple of two strings: the first is the name of the local non-DST timezone,
# the second is the name of the local DST timezone.

# time.timezone:
# The int offset of the local (non-DST) timezone, in seconds west of UTC
# (negative in most of Western Europe, positive in the US, zero in the UK).

print(f'timezone is {time.tzname[0]} with offset of {time.timezone} seconds')
# timezone is PST with offset of 28800 seconds

if time.daylight != 0:
    print('\tDST is in effect')
    print('\tThe DST timezone is ' + time.tzname[1])
    print(f'\tOffset is actually {time.timezone - (60 * 60)} seconds')
    # DST is in effect
    # The DST timezone is PDT
    # Offset is actually 25200 seconds

print('local time is ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print('UTC time is ' + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
# local time is 2017-11-07 16:28:23
# UTC time is 2017-11-08 00:28:23


# Read and Write Dates & Times with strftime() and strptime()
# -----------------------------------------------------------------------------
# isoformat() for date, time and datetime objects and, ctime() aren't the only
# way to write dates and times as strings. We can also convert dates and times
# to strings using strftime().

# This is provided as a METHOD in the datetime, date, and time objects, and
# as a FUNCTION in the time module. strftime() uses format strings to specify
# the output:

# %Y  year                          2017
# %y  year 0-99                     17
# %m  month                         08
# %B  month name                    August
# %b  month abbreviation            Aug
# %d  day of month                  16
# %A  weekday name                  Wednesday
# %a  weekday abbreviation          Wed
# %H  hour (24 hr)                  15
# %I  hour (12 hr)                  03
# %p  AM/PM                         PM
# %M  minute                        59
# %S  second                        59
# %f  microsecond as a decimal      886007
# %c  date and time                 Wed Aug 30 17:26:39 2017
# %x  date                          08/30/17
# %X  time                          17:26:39
# %j  day in 1-366                  242
# %U  week in 1-53 (Sun start)      35
# %W  week in 1-53 (Mon start)      35
# %w  weekday as a decimal 0-6      3
# %z  time zone offset from UTC     -0700  ** Doesn't work with all libraries
# %Z  time zone name                PDT    ** Deprecated

# NOTE: Time zone offset indicates a positive or negative time difference from
# UTC of the form +HHMM or -HHMM, where H represents decimal hour digits and M
# represents decimal minute digits [-23:59, +23:59].

# Here's the strftime() FUNCTION with the time module. It converts a
# struct_time object to a string:

import time

# For this method a Tuple or struct_time argument is required at 'a_time':

format = "It's %A, %B %d, %Y, local time: %I:%M:%S%p"

a_time = time.localtime()

print(time.strftime(format, a_time))
# It's Tuesday, November 07, 2017, local time: 04:28:23PM

# Here's the strftime() METHOD with a date object (the time defaults to midnight):

a_date = date(2017, 8, 16)

print(a_date.strftime(format))
# It's Wednesday, August 16, 2017, local time: 12:00:00AM

# If we try with a time object, we get a default date of 1900-01-01.

import datetime

a_dt_time = datetime.time(12, 3, 0)

print(a_dt_time.strftime(format))
# It's Monday, January 01, 1900, local time: 12:03:00PM

# Another way to write it:

datetime_string = datetime.datetime.now().strftime('%m-%d-%Y, %H:%M %p')

print(datetime_string)  # 12-31-2017, 10:47 AM

# To go the other way and convert a string to a date or time, use strptime()
# the nonformat parts of the string (without %) need to match EXACTLY.
# Example: specify a format that matches year-month-day, such as 2017-08-16.

format = '%Y-%m-%d'
a_date = time.strptime('2017-08-16', format)

print(a_date)
# time.struct_time(tm_year=2017, tm_mon=8, tm_mday=16, tm_hour=0, tm_min=0,
# tm_sec=0, tm_wday=2, tm_yday=228, tm_isdst=-1)

# NOTE: strptime is actually super useful when working with databases.
# For example, if you create a DateTime type column in an sqlite3 database,
# it will require a datetime object but depending on how you retrieve the
# data, my return a date string. Using strptime, you can convert these
# strimgs back again:

n = datetime.datetime.now()  # 2019-07-08 09:57:26.976697 <class 'datetime.datetime'>
s = str(n)
f = '%Y-%m-%d %H:%M:%S.%f'
d = datetime.datetime.strptime(s, f)

print(s, type(s))  # 2019-07-08 09:57:26.976697 <class 'str'>
print(d, type(d))  # 2019-07-08 09:57:26.976697 <class 'datetime.datetime'>


# locale module
# -----------------------------------------------------------------------------
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
    # Tuesday, October 31
    # Mardi, octobre 31
    # Dienstag, Oktober 31
    # martes, octubre 31
    # þriðjudagur, október 31

# The above does english, french, german, spanish, icelandic. For a complete
# list of lang_country...

import locale
names = locale.locale_alias.keys()

# not all the names work with setlocale(). The ones we're looking for are a
# two character language code followed by '_' and two character country code:

useable_names = [name for name in names if len(name) == 5 and name[2] == '_']
print(useable_names)
# ['a3_az', 'aa_dj', 'aa_er', 'aa_et', 'af_za', 'am_et', 'an_es', 'ar_aa',
# 'ar_ae', 'ar_bh', 'ar_dz', 'ar_eg', 'ar_in', 'ar_iq', 'ar_jo', 'ar_kw',
# 'ar_lb', 'ar_ly', 'ar_ma', 'ar_om', 'ar_qa', 'ar_sa', 'ar_sd', 'ar_sy',
# 'ar_tn', 'ar_ye', 'as_in', 'az_az', 'be_by', 'bg_bg', 'bn_bd', 'bn_in',
# 'bo_cn', 'bo_in', 'br_fr', 'bs_ba', 'ca_ad', 'ca_es', 'ca_fr', 'ca_it',
# 'cs_cs', 'cs_cz', 'cv_ru', 'cy_gb', 'cz_cz', 'da_dk', 'de_at', 'de_be',
# 'de_ch', 'de_de', 'de_lu', 'dv_mv', 'dz_bt', 'ee_ee', 'el_cy', 'el_gr',
# 'en_ag', 'en_au', 'en_be', 'en_bw', 'en_ca', 'en_dk', 'en_gb', 'en_hk',
# 'en_ie', 'en_in', 'en_ng', 'en_nz', 'en_ph', 'en_sg', 'en_uk', 'en_us',
# 'en_za', 'en_zm', 'en_zw', 'eo_eo', 'eo_xx', 'es_ar', 'es_bo', 'es_cl',
# 'es_co', 'es_cr', 'es_cu', 'es_do', 'es_ec', 'es_es', 'es_gt', 'es_hn',
# 'es_mx', 'es_ni', 'es_pa', 'es_pe', 'es_pr', 'es_py', 'es_sv', 'es_us',
# 'es_uy', 'es_ve', 'et_ee', 'eu_es', 'eu_fr', 'fa_ir', 'ff_sn', 'fi_fi',
# 'fo_fo', 'fr_be', 'fr_ca', 'fr_ch', 'fr_fr', 'fr_lu', 'fy_de', 'fy_nl',
# 'ga_ie', 'gd_gb', 'gl_es', 'gu_in', 'gv_gb', 'ha_ng', 'he_il', 'hi_in',
# 'hr_hr', 'ht_ht', 'hu_hu', 'hy_am', 'ia_fr', 'id_id', 'ig_ng', 'ik_ca',
# 'in_id', 'is_is', 'it_ch', 'it_it', 'iu_ca', 'iw_il', 'ja_jp', 'jp_jp',
# 'ka_ge', 'kk_kz', 'kl_gl', 'km_kh', 'kn_in', 'ko_kr', 'ks_in', 'ku_tr',
# 'kw_gb', 'ky_kg', 'lb_lu', 'lg_ug', 'li_be', 'li_nl', 'lo_la', 'lt_lt',
# 'lv_lv', 'mg_mg', 'mi_nz', 'mk_mk', 'ml_in', 'mn_mn', 'mr_in', 'ms_my',
# 'mt_mt', 'my_mm', 'nb_no', 'ne_np', 'nl_aw', 'nl_be', 'nl_nl', 'nn_no',
# 'no_no', 'nr_za', 'ny_no', 'oc_fr', 'om_et', 'om_ke', 'or_in', 'os_ru',
# 'pa_in', 'pa_pk', 'pd_de', 'pd_us', 'ph_ph', 'pl_pl', 'pp_an', 'ps_af',
# 'pt_br', 'pt_pt', 'ro_ro', 'ru_ru', 'ru_ua', 'rw_rw', 'sa_in', 'sc_it',
# 'sd_in', 'sd_pk', 'se_no', 'sh_hr', 'sh_sp', 'sh_yu', 'si_lk', 'sk_sk',
# 'sl_cs', 'sl_si', 'so_dj', 'so_et', 'so_ke', 'so_so', 'sp_yu', 'sq_al',
# 'sq_mk', 'sr_cs', 'sr_me', 'sr_rs', 'sr_sp', 'sr_yu', 'ss_za', 'st_za',
# 'sv_fi', 'sv_se', 'sw_ke', 'sw_tz', 'ta_in', 'ta_lk', 'te_in', 'tg_tj',
# 'th_th', 'ti_er', 'ti_et', 'tk_tm', 'tl_ph', 'tn_za', 'tr_cy', 'tr_tr',
# 'ts_za', 'tt_ru', 'ug_cn', 'uk_ua', 'ur_in', 'ur_pk', 'uz_uz', 've_za',
# 'vi_vn', 'wa_be', 'wo_sn', 'xh_za', 'yi_us', 'yo_ng', 'zh_cn', 'zh_hk',
# 'zh_sg', 'zh_tw', 'zu_za']

# if you wanted all the german names:

de_names = [name for name in useable_names if name.startswith('de')]
print(de_names)  # ['de_at', 'de_be', 'de_ch', 'de_de', 'de_lu']

# language codes - https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
# country codes - https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2


# Measuring time
# -----------------------------------------------------------------------------
# A quick way of timing something is to get the current time, do something, get
# the new time, and then subtract the original time from the new time.

# time()

# from time import time as my_timer
# this does an ok job but in this application could end up with problems - if
# DST happens during that timing or the OS might have its internal clock synced
# with a time server.

# perf_counter()

# from time import perf_counter as my_timer
# perf_counter (for performance counter) is the most precise timer. It gives
# a highly accurate measure of the elapsed time - often used for benchmarking
# code. Note, the value returned doesn't represent an actual time.

# process_time()

# from time import process_time as my_timer
# This returns the value (in fractional seconds) of the sum of the system and
# user CPU time of the current process (not the actual elapsed time). It does
# not include time elapsed with sleep. Is apparently useful for profiling code.

import time
# from time import time as my_timer          # try all three
# from time import perf_counter as my_timer  # try all three
from time import process_time as my_timer  # try all three
import random

input('Press enter to start')
wait_time = random.randint(1,6)
time.sleep(wait_time)
start_time = my_timer()

input('Press enter to stop')
end_time = my_timer()

print('Elapsed time: {} seconds'.format(end_time - start_time))
# Elapsed time: 0.3398411273956299 seconds    (time)
# Elapsed time: 0.4680702360055875 seconds    (perf_counter)
# Elapsed time: 9.800000000000086e-05 seconds (process_time)

# Extra formatting review:
# (these only work with time module above, not perf_counter or process_time):

# convert epoch time (time.time()) to string using ctime():
# print('started at:', time.ctime(start_time))
# print('ended at:', time.ctime(end_time))

# convert epoch time (time.time()) to a struct_time (time.localtime())
# to a string using strftime():
# print('started at:', time.strftime("%X", time.localtime(start_time)))
# print('ended at:', time.strftime("%X", time.localtime(end_time)))

# Summary:
# Use time() when you want to record actual time.
# Use perf_counter() when you want to record elapsed time
# use process_time() when you want to record elapsed CPU time


# time.get_clock_info()
# -----------------------------------------------------------------------------
# argument names that can be used:
# – 'monotonic': time.monotonic()
# – 'perf_counter': time.perf_counter()
# – 'process_time': time.process_time()
# – 'time': time.time()

import time

monotonic_i = time.get_clock_info('monotonic')
perfcounter_i = time.get_clock_info('perf_counter')
processtime_i = time.get_clock_info('process_time')
time_i = time.get_clock_info('time')

print(monotonic_i)
# namespace(adjustable=False, implementation='mach_absolute_time()',
#   monotonic=True, resolution=1e-09)
print(perfcounter_i)
# namespace(adjustable=False, implementation='mach_absolute_time()',
#   monotonic=True, resolution=1e-09)
print(processtime_i)
# namespace(adjustable=False, implementation='getrusage(RUSAGE_SELF)',
#   monotonic=True, resolution=1e-06)
print(time_i)
# namespace(adjustable=True, implementation='gettimeofday()',
#   monotonic=False, resolution=1e-06)


# Alternative Modules
# -----------------------------------------------------------------------------
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
