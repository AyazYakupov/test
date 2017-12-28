import random
from random import choice
from string import ascii_letters
from string import digits
import re

def func():
    string = 'превет, я Коля. А как тибя звать'
    strlst = list(filter(None, re.split(r'[,. ]', string)))
    lst = ['как', 'я','тебя','А','звать','привет','Коля']
    for word in range(len(strlst)):
        for lword in range(len(lst)):
            if getDistance(strlst[word],lst[lword]) == 1:
                print(lst[lword], strlst[word])
                strlst[word] = lst[lword]
    return strlst

def getDistance(word,lword):
    if len(word) != len(lword) or len(word)<3:
        return 100
    dist = 0
    for letter in range(len(word)):
        if word[letter] != lword[letter]:
            dist += 1
    return dist


print(func())
