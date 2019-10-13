''' Date and Time '''

# Calendar Module

import calendar

s = input().split()

month = int(s[0])
day = int(s[1])
year = int(s[2])

week_i = calendar.weekday(year, month, day)
day = str(calendar.day_name[week_i])
print(day.upper())


#Time Delta
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
import datetime
import calendar

def get_utc_timestamp(t1):
    tokens = t1.split()
    year = int(tokens[3])
    month = list(calendar.month_abbr).index(tokens[2])
    day = int(tokens[1])

    timestamp = tokens[4].split(':')
    hours = int(timestamp[0])
    minutes = int(timestamp[1])
    seconds = int(timestamp[2])

    a = datetime.datetime(year, month, day, hours, minutes, seconds, 0)
    
    tz = tokens[5]
    sign = tz[0]
    h_tz = int(tz[1]+tz[2])
    m_tz = int(tz[3]+tz[4])

    conversion_fact = h_tz * 3600 + m_tz * 60
    if sign == '+':
        conversion_fact *= -1


    return a.timestamp() + conversion_fact

def time_delta(t1, t2):
    t1_ts = get_utc_timestamp(t1)
    t2_ts = get_utc_timestamp(t2)

    delta = abs(t1_ts - t2_ts)
    return str('%d' % delta)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
