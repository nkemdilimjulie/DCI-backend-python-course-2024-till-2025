
import datetime as dt

# concert_date = dt.datetime(2024, 8, 22, 20, 30, 44)

# concert_date = dt.datetime.fromisoformat('2024-08-22 20:30:44')

concert_date = dt.datetime.fromisoformat('2024-08-22T20:30:44')

# print(concert_date)


# Calendar 

# import calendar


# calendar_2024 = calendar.calendar(2024)

# print(calendar_2024)


# Calendar 

import calendar


calendar_2024 = calendar.calendar(2024)

# print(calendar_2024)


# calendar.setfirstweekday(1)

calendar_month = calendar.month(2024, 7)

# print(calendar_month)

# calendar_month = calendar.month(2025, 10, 8) # adding some width


# print(calendar_month)

# print(calendar.firstweekday())


# print(calendar.isleap(2024))

# print(2024 / 4)

# print(2024 / 100)

# print(2024 / 400)

# print(2100 / 4)

# print(2100 / 100)

# print(2100 / 400)

# print(2000 / 4)

# print(2000 / 100)

# print(2000 / 400)



cal = calendar.TextCalendar()

cal_2024 = cal.formatyear(2024)

# print(cal_2024)


cal_2024_july = cal.formatmonth(2024, 7)

# print(cal_2024_july)


cal2 = calendar.HTMLCalendar()

cal_html_month = cal2.formatmonth(2025, 7)

# print(cal_html_month)

cal_html = cal2.formatyear(2025)


print(cal_html)

x = 'lunch time'

print(x)


# Not working


# cal_2024_week = cal.formatweek(2024, 5, 3)

# print(cal_2024_week)

# print(cal.prweek())

# print(cal.formatweek(5, 10))

# for week in cal.monthdays2calendar(2024, 7):
#     print(cal.formatweek(week, 1))


