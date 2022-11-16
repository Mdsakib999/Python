
import calendar

print("Entter a date M/D/Y :")
m, d, y = map(int, input().strip().split())

print(calendar.day_name[calendar.weekday(y, m, d)].upper())




"""
#to find a fixed month of a year.

import calendar
y = 2022
m = 8
print(calendar.month(y, m))
"""

"""
import datetime
import calendar
m, d, y = map(int, input().split())
input_date = datetime.date(y, m, d)
print(calendar.day_name[input_date.weekday()].upper())

"""