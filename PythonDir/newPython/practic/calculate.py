import random
from random import choice
from string import ascii_letters
from string import digits
import re
def func():
    string = '28+(37*(2/2)-33)+(20/10)*22*(2.3+32)'
    tr = int('-28')
    while re.search(r'(?<=\()(\d+(\.\d+)?[+-|\*|\/])+\d+(\.\d+)?(?=\))',string):
        start = re.search(r'(?<=\()(\d+(\.\d+)?[+-|\*|\/])+\d+(\.\d+)?(?=\))',string).start()
        end = re.search(r'(?<=\()(\d+(\.\d+)?[+-|\*|\/])+\d+(\.\d+)?(?=\))',string).end()
        newstr = string[start:end]
        newstr = operFirst(newstr)
        newstr = operSecond(newstr)
        string = string[:start-1] + str(newstr) + string[end+1:]
    string = operFirst(string)
    string = operSecond(string)
    return string

def operFirst(newstr):
    while re.search(r'\d+(\.\d+)?(\*|\/)\d+(\.\d+)?', newstr):
        st = re.search(r'\d+(\.\d+)?(\*|\/)\d+(\.\d+)?', newstr).start()
        en = re.search(r'\d+(\.\d+)?(\*|\/)\d+(\.\d+)?', newstr).end()
        nwstr = newstr[st:en]
        nwstr = decision(newstr[st:en])
        newstr = newstr[:st] + str(nwstr) + newstr[en:]
    return newstr
def operSecond(newstr):
    while re.search(r'\d+(\.\d+)?[+-]\d+(\.\d+)?', newstr):
        st = re.search(r'\d+(\.\d+)?[+-]\d+(\.\d+)?', newstr).start()
        en = re.search(r'\d+(\.\d+)?[+-]\d+(\.\d+)?', newstr).end()
        nwstr = newstr[st:en]
        nwstr = decision(newstr[st:en])
        newstr = newstr[:st] + str(nwstr) + newstr[en:]
    return newstr
        
def decision(nwstr):
    lst = re.split(r'[+-]|\*|\/', nwstr)
    if '+' in nwstr:
        nwstr = str(float(lst[0])+float(lst[1]))
    if '-' in nwstr:
        nwstr = str(float(lst[0])-float(lst[1]))
    if '*' in nwstr:
        nwstr = str(float(lst[0])*float(lst[1]))
    if '/' in nwstr:
        nwstr = str(float(lst[0])/float(lst[1]))
    return nwstr

def newfunc():
    lst = re.findall(r'(-?\d+\.?\d+?)', '28.0-(-23.0)')
    return lst

print(func())
