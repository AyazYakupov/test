def is_year_leap(year: int):
    if year % 4 or year % 100 == 0:
        return False
    else:
        return True

year = int(input('введите год: '))
if is_year_leap(year):
    print('Год високосный')
else:
    print('Год не високосный')
