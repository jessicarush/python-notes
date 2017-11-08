'''Calendars & Clocks'''

# Working with dates and times can be a bit of a pain on account of varying
# formats, time zones, daylight savings times, and so on. Python's standard
# library has many date and time modules: datetime, time, calendar, locale
# and others. There's some overlap, and a bit confusing:

# calendar module:
#   General calendar-related functions.

# datetime module:
#   Object-oriented interface to dates and times with similar functionality
#   to the time module.

# time module:
#   Low-level time related functions (time access and conversions)
#
# locale module:
#   Internationalization services. The locale setting affects the
#   interpretation of many format specifiers in strftime() and strptime().

# -----------------------------------------------------------------------------
# calendar module
# -----------------------------------------------------------------------------

import calendar

# test if a year is a leap year:
print(calendar.isleap(2016))  # True
print(calendar.isleap(2017))  # False

# -----------------------------------------------------------------------------
# datetime module
# -----------------------------------------------------------------------------
# Note with datetime objects some are considered naive and some are aware.
# Aware objects are aware of the timezone offset and naive objects are not.

# The datetime module defines four main objects, each with many methods:
# – datetime.date() for years, months, days
# – datetime.time() for hours, minutes, seconds, and fractions
# – datetime,datetime() for dates and times together
# – datetime.timedelta() for date and/or time intervals

# -----------------------------------------------------------------------------
# datetime.date()
# -----------------------------------------------------------------------------
# make a date() object by specifying a year, month, and day.
# Those values are then available as attributes:

from datetime import date

halloween = date(2017, 10, 31)
print(halloween.day)    # 31
print(halloween.month)  # 10
print(halloween.year)   # 2017

# print a date with isoformat() method:

print(halloween.isoformat())  # 2017-10-31

# The iso refers to ISO 8601, an international standard for representing dates
# and times. It goes from most general (year) to most specific (day). It also
# sorts correctly: by year, then month, then day.

# weekday() method tells you the day of the week.
# Monday is 0, Sunday is 6

print(halloween.weekday())  # 1 (Tuesday)

# today() method to generate today's date:

from datetime import date
now = date.today()
print(now)  # 2017-11-07

# -----------------------------------------------------------------------------
# datetime.timedelta()
# -----------------------------------------------------------------------------
# A timedelta() object can be used to add a time interval to a date:

from datetime import timedelta

one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)          # 2017-11-08
print(now + 18*one_day)  # 2017-11-25

# subtracting two dates will give you a timedelta object:

time_diff = halloween - now
print(time_diff)        # -7 days, 0:00:00
print(type(time_diff))  # <class 'datetime.timedelta'>

# Note: The range of date is from date.min (year=1, month=1, day=1) to
# date.max (year=9999, month=12, day=31). As a result, you can't use it for
# historic or astronomical calculations.

# See also: timedelta_example.py

# -----------------------------------------------------------------------------
# datetime.time()
# -----------------------------------------------------------------------------
# The datetime module's time() object is used to represent a time of day:

from datetime import time

noon = time(12, 0, 1)

print(noon.hour)         # 12
print(noon.minute)       # 0
print(noon.second)       # 1
print(noon.microsecond)  # 0

# The arguments go from the largest time unit (hours) to the smallest
# (microseconds). If you don't provide all the arguments, time assumes all the
# rest are zero.

# -----------------------------------------------------------------------------
# datetime.datetime()
# -----------------------------------------------------------------------------
# The datetime() object includes both the date and time of day. The following
# would be for August 16, 2017, at 2:09 P.M., plus 5 seconds, 6 microseconds:

from datetime import datetime

a_day = datetime(2017, 8, 16, 14, 9, 5, 6)

# The datetime object also has an isoformat() method:

print(a_day.isoformat())  # 2017-08-16T14:09:05.000006

# datetime has methods with which you can get the current date and time, utc:

print(datetime.today())   # 2017-11-07 16:17:15.343399
print(datetime.now())     # 2017-11-07 16:17:15.343410
print(datetime.utcnow())  # 2017-11-08 00:17:15.343416

# now() and today() are similar. now() allows us to provide timezone with a
# tzinfo object (see timezones.py)

now = datetime.now()

print(now.isoformat())  # 2017-11-07T16:18:22.570422
print(now.year)         # 2017
print(now.month)        # 11
print(now.day)          # 7
print(now.hour)         # 16
print(now.minute)       # 18
print(now.second)       # 22
print(now.microsecond)  # 570422

# You can merge a date object and a time object into a datetime object by
# using combine():

from datetime import datetime, time, date

noonish = time(12, 3, 0)
this_day = date.today()
noonish_today = datetime.combine(this_day, noonish)

print(noonish_today)       # 2017-11-07 12:03:00
print(type(noonish_today)) # <class 'datetime.datetime'>

# You can pull the date and time out from a datetime object by using the
# date() and time() methods:

print(noonish_today.date()) # 2017-11-07
print(noonish_today.time()) # 12:03:00

# -----------------------------------------------------------------------------
# Time module
# -----------------------------------------------------------------------------
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

import time

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

print(('Year {0[0]}, Month {0[1]}, Day {0[2]}, Hour {0[3]}, Minute {0[4]}, '
       'Second {0[5]}, Weekday {0[6]}, Yearday {0[7]}, DST {0[8]}').format(t))
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

# -----------------------------------------------------------------------------
# Timezones and DST
# -----------------------------------------------------------------------------

import time

# time.tzname[]:
# A tuple of two strings: the first is the name of the local non-DST timezone,
# the second is the name of the local DST timezone.

# time.timezone:
# The int offset of the local (non-DST) timezone, in seconds west of UTC
# (negative in most of Western Europe, positive in the US, zero in the UK).

print('current timezone is {0} with offset of {1} seconds'.format(
       time.tzname[0], time.timezone))
# current timezone is PST with offset of 28800 seconds

if time.daylight != 0:
    print('\tDST is in effect')
    print('\tThe DST timezone is ' + time.tzname[1])
    print('\tOffset is actually {} seconds'.format(time.timezone - (60 * 60)))
    # DST is in effect
    # The DST timezone is PDT
    # Offset is actually 25200 seconds

print('local time is ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print('UTC time is ' + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
# local time is 2017-11-07 16:28:23
# UTC time is 2017-11-08 00:28:23

# -----------------------------------------------------------------------------
# Read and Write Dates & Times
# -----------------------------------------------------------------------------
# isoformat() for date, time and datetime objects and, ctime() for epochs
# aren't the only way to write dates and times as strings. We can also convert
# dates and times to strings using strftime().

# This is provided as a method in the datetime, date, and time objects, and
# as a function in the time module. strftime() uses format strings to specify
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

# Here's the strftime() function with the time module. It converts a
# struct_time object to a string:

import time

fmt = "It's %A, %B %d, %Y, local time: %I:%M:%S%p"

t = time.localtime()

# Emphasis: for this method Tuple or struct_time argument required at 't':
print(time.strftime(fmt, t))
# It's Tuesday, November 07, 2017, local time: 04:28:23PM

# If we try with a date object, the time defaults to midnight:
a_day = date(2017, 8, 16)
print(a_day.strftime(fmt))
# It's Wednesday, August 16, 2017, local time: 12:00:00AM

# If we try with a time object, we get a default date of 1900-01-01
# have to import again otherwise it will try to use time from import time
from datetime import time

a_time = time(12, 3, 0)
print(a_time.strftime(fmt))
# It's Monday, January 01, 1900, local time: 12:03:00PM

# To go the other way and convert a string to a date or time, use strptime()
# the nonformat parts of the string (without %) need to match EXACTLY.
# Example: specify a format that matches year-month-day, such as 2017-08-16.

import time

fmt = '%Y-%m-%d'
a_date = time.strptime('2017-08-16', fmt)
print(a_date)
# time.struct_time(tm_year=2017, tm_mon=8, tm_mday=16, tm_hour=0, tm_min=0,
# tm_sec=0, tm_wday=2, tm_yday=228, tm_isdst=-1)

# -----------------------------------------------------------------------------
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

# -----------------------------------------------------------------------------
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
from time import process_time as my_timer  # try all three above
import random

input('Press enter to start')
wait_time = random.randint(1,6)
time.sleep(wait_time)
start_time = my_timer()

input('Press enter to stop')
end_time = my_timer()

print('Elapsed time: {} seconds'.format(end_time - start_time))
# Elapsed time: 0.00011199999999999405 seconds

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

# -----------------------------------------------------------------------------
# time.get_clock_info()
# -----------------------------------------------------------------------------
# argument names that can be used:
# – 'clock': time.clock()
# – 'monotonic': time.monotonic()
# – 'perf_counter': time.perf_counter()
# – 'process_time': time.process_time()
# – 'time': time.time()

import time

clock_i = time.get_clock_info('clock')
monotonic_i = time.get_clock_info('monotonic')
perfcounter_i = time.get_clock_info('perf_counter')
processtime_i = time.get_clock_info('process_time')
time_i = time.get_clock_info('time')

print(type(clock_i)) # <class 'types.SimpleNamespace'>

print(clock_i)
# namespace(adjustable=False, implementation='clock()',
#   monotonic=True, resolution=1e-06)
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

# -----------------------------------------------------------------------------
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
