
import datetime as dt

now = dt.datetime.now()

today = dt.datetime.today()

# print(now)
# print(today)


birth_date = dt.date(2004, 11, 22)

birth_datetime = dt.datetime(2004, 11, 22, 10, 30, 44)


event_date = dt.date(year=2024, month=8, day=16)

event_datetime = dt.datetime(year=2024, day=16, month=8, hour=10, minute=30, second=44)


# print(event_date.year)
# print(event_date.month)

# print(event_datetime.year)

# print(event_datetime.weekday()) # monday = 0, tuesday = 1, wednesday = 2,....sunday = 6


# timedelta

# difference_days = dt.timedelta(35)

difference_days = dt.timedelta(days=35, hours=2, minutes=20)

# future_date = event_date + difference_days

# print(event_date)
# print(future_date)


future_datetime = event_datetime + difference_days

# print(event_datetime)
# print(future_datetime)



# print(event_date)
# print(event_datetime)


# print(type(event_date))
# print(type(event_datetime))


# past_datetime = today - dt.timedelta(days=9)

past_datetime = today - dt.timedelta(weeks=1)

# print(past_datetime)




valentines_day = dt.datetime(year=2024, month=2, day=14)

# print(valentines_day)


# print(dir(dt.datetime))

valentines_datetime = dt.datetime(year=2024, month=2, day=14, hour=20, minute=30)

# print(valentines_datetime)

text = 'This year valentines day was on 14th of February, 2024.'

text_datetime = dt.datetime.strptime(text, 'This year valentines day was on %dth of %B, %Y.')

# print(text_datetime)

vacation = '2024/Jul/28 14:20:33'

vacation_datetime = dt.datetime.strptime(vacation, '%Y/%b/%d %H:%M:%S')

print(vacation_datetime)


# travel_text = dt.datetime.strftime(vacation_datetime, 'We will travel on %Y/%b/%d %H:%M:%S')

travel_text = dt.datetime.strftime(vacation_datetime, 'We will travel on %dth %B, %Y at %I:%M:%S %p.') # same as next one

travel_txt = vacation_datetime.strftime('We will travel on %dth %B, %Y at %I:%M:%S %p.') # same as before


print(travel_text)
print(travel_txt)

