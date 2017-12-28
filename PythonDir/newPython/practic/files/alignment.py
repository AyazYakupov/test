import sys
import re
def OpenFile(file_name, mod):
    try:
        the_file = open(file_name, mod)
    except IOError as e:
        print('Невозможно открыть файл - ',file_name,'. Работа программы будет завершена. \n', e)
    else:
        return the_file
def ReadFile(the_file):
    lst = []
    for line in the_file:
        lst.append(line.strip())
    return lst
def Counter(lst):
    mx = max(lst)
    mxlen = len(mx)
    for i in range(len(lst)):
        if mx in lst[i]:
            lst[i] = ' '*5 + lst[i]+'\n'
        else:
            lst[i] = ' '*(5-len(lst[i])+mxlen) + lst[i] + '\n'
    return lst
def ToString(lst):
    string = ''.join(lst)
    return string


def Main():
    the_file = OpenFile('input.txt','r')
    lst = ReadFile(the_file)
    lst = Counter(lst)
    print(ToString(lst))



Main()

