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
    dictionary = {}
    lines = 1
    for line in the_file:
        if line:
            dictionary.update({str(lines):re.findall(r'\d+', line)})
        lines += 1
    return dictionary
def WriteFile(the_file, dictionary):
    lst = []
    for i in dictionary.keys():
        for j in dictionary[i]:
            lst.append([i,j])
    lst.sort(key=lambda x: int(x[1]))
    for i in lst:
        the_file.write(i[1]+' '+i[0]+'\n')


        
def Main():
    the_file = OpenFile('input.txt','r')
    dictionary = ReadFile(the_file)
    the_file = OpenFile('output.txt','w')
    WriteFile(the_file,dictionary)

Main()

