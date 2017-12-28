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
        lst.append(re.findall(r'\w+',line))
    the_file.close()
    return lst
def Compare(lst):
    compareLst = []
    for position in lst:
        compareLst.append(int(position[0])+int(position[1]))
    mx = max(compareLst)
    mn = min(compareLst)
    indmx = compareLst.index(mx)
    indmn = compareLst.index(mn)
    return (lst[indmx], lst[indmn])
def Write(the_file,result):
    the_file.write(str(result))
    print('Записано')
    return 0
the_file = OpenFile('input.txt','r')
lst = ReadFile(the_file)
result = Compare(lst)
the_file = OpenFile('output.txt','w')
Write(the_file,result)
