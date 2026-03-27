# Python datetime
# Get the current day, month, year, hour, minute and timestamp from datetime module
import datetime
from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
seconds = now.second
timestamp = now.timestamp
print(day,month,year,hour,minute,seconds,timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}:{seconds}')
# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
now = datetime.now()
format_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(format_date)
# Today is 5 December, 2019. Change this time string to time.
Today_date = datetime.strptime('5 December, 2019', '%d %B, %Y')
print(Today_date)
# Calculate the time difference between now and new year.
now = datetime.now()
new_year = datetime(now.year + 1, 1, 1)
time_diff = new_year - now
print('The time differnce between now and new year is:', time_diff)

from datetime import date
today = date(year=2026, month=3, day=27)
new_year_date = date(year=2027, month=1, day=1)
day_diff = new_year_date - today
print('The days difference between now and new year is:', day_diff)

# Calculate the time difference between 1 January 1970 and now.
now = datetime.now()
date_to = datetime(1970,1,1)
diff_days = now - date_to
print(f'The time difference between now and 1970 is:{diff_days}')
print(f'The time difference between now and 1970 is:{diff_days.days}')
