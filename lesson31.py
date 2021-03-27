from datetime import date, datetime, timedelta
import locale

#date
# today =date.today()
# print(today) # 2021-03-20
# print(today.day, today.month, today.year)
# print(today.weekday())

#datetime
# now1 = datetime.now()
# now2 = datetime.today()
# print(now1, now2, sep='\n')

# locale.setlocale(locale.LC_ALL, 'uk_UA')
locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
# now = datetime.now()
# print(now)
# print(now.strftime('%A'))

# print(f'Дата: {now.strftime("%A, %d %B %Y")}')
# print(f'Час: {now.strftime("%H:%M:%S")}')
# print(now.strftime('%c'))
# print(now.strftime('%x'))
# print(now.strftime('%X'))

#timedelta
now = datetime.now()
print(now.strftime('%c'))
d1 = now + timedelta(days=1, hours=5, minutes=15)
print(d1.strftime('%c'))