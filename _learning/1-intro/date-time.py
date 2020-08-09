#!/usr/bin/python3

################################################################
# Text
################################################################

import time
from datetime import datetime


time.localtime(time.time()) # local time
time.asctime(time.localtime(time.time()))
time.gmtime(time.time()) # time in UTC
#alternatively
str(datetime.now())

#import time
time.localtime()
print('Day:',time.localtime().tm_mday) # output: Day: 6
print('Hour:',time.localtime().tm_hour) # output: Hour: 21
print('Minute:',time.localtime().tm_min) # output: Minute: 13
print('Second:',time.localtime().tm_sec) # output: Second: 11

rightnow = time.asctime(time.localtime()) # local time
print(rightnow) # Sat Mar 21 22:56:53 2020
# time.gmtime(time.localtime()) # time in UTC

# formatting date time
from datetime import datetime
'{:%d-%b-%Y %I:%M:%S %p}'.format(datetime.now())
# output: '06-Apr-20118 09:39:10 PM'

'{:%d/%m/%Y %H:%M:%S}'.format(datetime.now())
# output: '06/04/20118 21:39:25'

# time delta
from datetime import datetime, timedelta

# timedelta and future/past dates
futuredate = datetime.now() + timedelta(days=365, hours=4, minutes=2)
pastdate = datetime.now() + timedelta(days=-365,  hours=4, minutes=2)

'{:%d-%b-%Y %I:%M:%S %p}'.format(futuredate)

'{:%d-%b-%Y %I:%M:%S %p}'.format(pastdate)
