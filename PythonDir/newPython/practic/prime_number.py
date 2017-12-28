def prime_number(x: int):
    if x == 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

nb = int(input('введите число: '))
if prime_number(nb):
    print('число {} является простым'.format(str(nb)))
else:
    print('число {} не является простым'.format(str(nb)))
