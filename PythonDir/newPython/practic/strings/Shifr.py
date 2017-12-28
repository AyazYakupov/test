import random
from random import choice
from string import ascii_letters
from string import digits
import re
import rsa

def func():
    string = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

    stringToLst = string.split()
    alphabit = 'abcdefghijklmnopqrstuvwxyz'
    lst2 = []
    offset = 1
    for i in range(len(alphabit)):
        lst2.append([alphabit[i],alphabit[i-offset]])

    count = 3
    for word in range(len(stringToLst)):
        newstr = ''
        mystr = ''
        for i in stringToLst[word]:
            for j in range(len(lst2)):
                if i.lower() == lst2[j][0]:
                    newstr += lst2[j][1]
                if i == '/':
                    newstr += '\\n'
                    # count += 1
                    break
                # if i == ' ':
                #     newstr += ' '
                #     break
        for i in range(len(newstr)):
            if len(newstr) > 2:
                mystr += newstr[i-count]
            else: mystr += newstr[i-1]
        stringToLst[word] = mystr
        
        string = ' '.join(stringToLst)
    return string

print(func())
