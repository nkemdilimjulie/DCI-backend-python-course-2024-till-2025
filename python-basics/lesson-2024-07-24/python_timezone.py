
import datetime as dt

# from datetime import datetime, timedelta, time # datetime.datetime

holiday = dt.datetime(2024, 7, 27, 10, 30, 44)

holiday_timestamp = holiday.timestamp()

# holiday_2 = datetime(2024, 7, 27, 10, 30, 44)

# datetime.
# dt.

# print(holiday)
# print(holiday_timestamp)
# print(holiday_2)


early_date_timestamp = dt.datetime(1970, 1, 1, 1, 0, 20).timestamp()

# print(early_date_timestamp)


# Find the current timestamp of your location.

current_timestamp = dt.datetime.now().timestamp()

# print(current_timestamp)


time_seconds = 2314832170

# time_seconds_datetime = dt.datetime.fromtimestamp(1154355363)

time_seconds_datetime = dt.datetime.fromtimestamp(time_seconds)

# print(time_seconds_datetime)

# print(time_seconds_datetime.strftime('Date: %Y/%m/%d \nTime: %H:%M:%S'))

# print(time_seconds_datetime.strftime('Date: %Y/%m/%d \nTime: %I:%M:%S %p'))


# Timezone


citric = dt.timedelta(hours=-7)

citric_tz = dt.timezone(citric)


# music_concert = dt.datetime(2024, 11, 22, 20, 30, 44, tzinfo=citric_tz)

# print(music_concert)


import dateutil.tz
import pytz

utc_tz = pytz.utc

eastern_tz = pytz.timezone('US/Eastern')

pacific_tz = pytz.timezone('Pacific/Fiji')

music_concert_utc = dt.datetime(2024, 11, 22, 20, 30, 44, tzinfo=utc_tz)

# music_concert_est = dt.datetime(2024, 11, 22, 20, 30, 44, tzinfo=eastern_tz)

music_concert_est = music_concert_utc.astimezone(eastern_tz)

music_concert_pcf = music_concert_utc.astimezone(pacific_tz)

music_concert_pcf2 = music_concert_est.astimezone(pacific_tz)


# print(music_concert_utc)
# print(music_concert_est)
# print(music_concert_pcf)
# print(music_concert_pcf2)


# Convert your current time to Kolkata time.

europe_tz = pytz.timezone('Europe/Berlin')

current_time = dt.datetime.now(tz=europe_tz)

kolkata_tz = pytz.timezone('Asia/Kolkata')

time_now_kolkata = current_time.astimezone(kolkata_tz)

# print(current_time)
# print(time_now_kolkata)

# europe_time = europe_tz.localize(dt.datetime.today())

# print(europe_time)


import dateutil

eu_tz = dateutil.tz.gettz('Europe/Berlin')

utc_tz = dateutil.tz.tzutc()

october_festival_eu = dt.datetime(2024, 10, 1, 16, 40, 20, tzinfo=eu_tz)

october_festival_utc = dt.datetime(2024, 10, 1, 16, 40, 20, tzinfo=utc_tz)

print(october_festival_eu)
print(october_festival_utc)

