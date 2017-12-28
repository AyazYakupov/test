import math
def square(x: int):
    lst = []
    lst.append(x*4)
    lst.append(x**2)
    lst.append(round(x*math.sqrt(2), 2))
    tpl = tuple(lst)
    return tpl

print(square(5))
