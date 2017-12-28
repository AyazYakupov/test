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
    string = the_file.read()
    ln = len(string)//3
    lst = []
    lst.append(list(string[:ln]))
    lst.append(list(string[ln:ln*2]))
    lst.append(list(string[ln*2:]))
    return lst
def Encoder(lst):
    encoded = []
    for j in range(len(lst[0])):
        encoded.append(lst[0][j])
        encoded.append(lst[1][j])
        encoded.append(lst[2][j])
    return encoded
def ToString(lst):
    string = ''.join(lst)
    return string
def Decoder(lst):
    decoded = []
    buf1 = []
    buf2 = []
    buf3 = []
    for i in range(0,len(lst),3):
        buf1.append(lst[i])
        buf2.append(lst[i+1])
        buf3.append(lst[i+2])
    decoded.extend(buf1)
    decoded.extend(buf2)
    decoded.extend(buf3)
    return decoded
def Main():
    the_file = OpenFile('input.txt','r')
    lst = ReadFile(the_file)
    lst = Encoder(lst)
    string = ToString(lst)
    print(string)
    lst = Decoder(lst)
    string = ToString(lst)
    print(string)
Main()

