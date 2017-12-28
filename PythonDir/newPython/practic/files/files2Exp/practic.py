import sys
import pickle
import re
import random as r
def OpenFile(file_name, mod):
    try:
        the_file = open(file_name, mod)
    except IOError as e:
        print('Невозможно открыть файл - ',file_name,'. Работа программы будет завершена. \n', e)
    else:
        return the_file
def GenIp(count):
    ips = []
    for i in range(count):
        lst = []
        ip = str(r.randint(0,1000))+'.'+str(r.randint(0,100))+'.'+str(r.randint(0,1000))+'.'+str(r.randint(0,1000))
        for j in range(r.randint(1,50)):
            lst.append(ip+' '+str(r.randint(1,24))+':'+str(r.randint(0,59))+':'+str(r.randint(0,59))+' '+r.choice(['Sunday','Monday','Tuesday','Wednesday','Thurday','Friday','Saturday'])+'\n')

        ips.append(lst)
    return ips
            
def WriteFile(f, lst):
    for item in lst:
        f.writelines(item)
    f.close()
    

def ReadFile(f):
    lst = []
    position = []
    for line in f:
        position.append(re.findall(r'\d+\.\d+\.\d+\.\d+',line))
        position.append(re.findall(r'\d+:\d+:\d+', line))
        position.append(re.findall(r'[a-zA-Z]+', line))
        lst.append(position)
        position = []
    return lst






def Main():
    the_file = OpenFile('input.txt','r')
    print(ReadFile(the_file))
    

Main()

