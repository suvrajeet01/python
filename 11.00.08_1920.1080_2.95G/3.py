#calender with python
import calendar

print(calendar.weekheader(1))
print()
print(calendar.weekheader(2))
print()
print(calendar.firstweekday())
print()
print(calendar.month(2020, 4))
print()
#calendar in matrix form
print(calendar.monthcalendar(2020, 4))
#printing out a whole year
print(calendar.calendar(2020))
a=day_of_the_week = calendar.weekday(2020, 4 ,11)
print (a)

print(calendar.weekday(2020, 4, 11))
print(calendar.isleap(2020))

print(calendar.leapdays(2000,2001))
print(calendar.leapdays(2000,2100))

print(calendar.leapdays(1800,2800))

print(calendar.leapdays(2000,3000))

import datetime
import time

