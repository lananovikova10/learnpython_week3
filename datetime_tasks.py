#Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
#Превратите строку "01/01/25 12:10:03.234567" в объект datetime
from datetime import datetime
from datetime import date
from datetime import timedelta

today = date.today()

yesterday = today - timedelta(days=1)
print(yesterday)
print(today)

thirty_days_before = today - timedelta(days=30)
print(thirty_days_before)

date_str = '01/01/25 12:10:03.234567'
parse_date = datetime.strptime(date_str, '%d/%m/%y %H:%M:%S.%f')
print(parse_date)
