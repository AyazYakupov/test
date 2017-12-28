def bank(a, year):
    for i in range(year):
        a = a*1.1
    return int(a)

money = int(input('введите количество рублей: '))
year = int(input('введите количество лет: '))
print('сумма вклада по окончанию {} будет равна {} рублей'.format(str(year), str(bank(money, year))))
