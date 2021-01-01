#!/usr/bin/env python3

################################################################
# Examples of date time
################################################################

import time
from datetime import datetime, timedelta

# Example 0: My normal date format
date = '{:%Y-%m-%d %I:%M:%S %p}'.format(datetime.now())
print(f"Example 0 - My normal date format: {date}")

# Example 1: print local time in format `Fri Jan  1 08:39:49 2021`
# local time
date = time.localtime(time.time())
# date currently holds an object `time.struct_time(tm_year=2021, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=38, tm_sec=31, tm_wday=4, tm_yday=1, tm_isdst=0)`
date = time.asctime(date)
print(f"Example 1: {date}")
# Returns `Fri Jan  1 08:39:49 2021`

# Using example 1, you could store each of the values in integers
# uncomment and run to test:
# time.localtime()
# print('Day:',time.localtime().tm_mday) # output: Day: 6
# print('Hour:',time.localtime().tm_hour) # output: Hour: 21
# print('Minute:',time.localtime().tm_min) # output: Minute: 13
# print('Second:',time.localtime().tm_sec) # output: Second: 11

# Example 2: print UTC time in format `Fri Jan  1 14:48:36 2021`
date = time.gmtime(time.time())
date = time.asctime(date)
print(f"Example 2: {date}")

# Example 3: print local time in format `2021-01-01 08:41:34.168579`
date = str(datetime.now())
print(f"Example 3: {date}")

# Example 4: Formating date time like '01-Jan-2021 08:54:27 AM'
date = '{:%d-%b-%Y %I:%M:%S %p}'.format(datetime.now())
print(f"Example 4: {date}")

# Example 5: Formating date time like '01/01/2021 08:55:36'
date = '{:%m/%d/%Y %H:%M:%S}'.format(datetime.now())
print(f"Example 5: {date}")

# Example 6: Using time delta (make sure to put from datetime import datetime, timedelta)
# Returns:
# One year in future `Example 6 - Future Date: 01-Jan-2022 01:01:17 PM`
# One year in the past `Example 6 - Past Date: 02-Jan-2020 01:01:17 PM`
futuredate = datetime.now() + timedelta(days=365, hours=4, minutes=2)
date = '{:%d-%b-%Y %I:%M:%S %p}'.format(futuredate)
print ( f"Example 6 - Future Date: {date}")

pastdate = datetime.now() + timedelta(days=-365,  hours=4, minutes=2)
date = '{:%d-%b-%Y %I:%M:%S %p}'.format(pastdate)
print ( f"Example 6 - Past Date: {date}")