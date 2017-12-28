import sys
import pickle
import re
def OpenFile(file_name, mod):
    try:
        the_file = open(file_name, mod)
    except IOError as e:
        print('Невозможно открыть файл - ',file_name,'. Работа программы будет завершена. \n', e)
    else:
        return the_file
            
def WriteFile(f,content):
    pickle.dump(content, f)
    

def ReadFile(f):
    content = pickle.load(f)
    return (content)
    # int16 = pickle.load(f)
    # name = pickle.load(f)
    # price = pickle.load(f)
    # scale = pickle.load(f)
    # gradiate = pickle.load(f)
    # regionscan = pickle.load(f)
    # print('количество записей: ',int16,'\nимя: ', name, '\nцена: ',price,'\nразрешение: ',scale, '\nградации серого: ',gradiate, '\nобласть сканирования: ',regionscan)
def ChangeContent(content, group, name, position, value):
    if PosDetect(position):
        position = PosDetect(position)
    else: return 'Ошибка позиции'
    content.get(group).get(name)[position-1] = value
    return content

def PosDetect(position):
    if position == 'price':
        return 1
    elif position == 'scale':
        return 2
    elif position == 'gradiate':
        return 3
    elif position == 'regionScan':
        return 4
    else: return 0


def Main():
    scans = {
        'Panasonic':{'Laserjet':['1800','1024*764','100','20*10'],'HyperPrint':['2400','1920*1080','200','30*15']},
        'Sony':{'Killjoy':['3000','1920*1080','250','30*15']}
        }
    full = [scans,len(scans)]
    the_file = OpenFile('output.txt','wb')
    WriteFile(the_file,full)
    the_file = OpenFile('output.txt','rb')
    full = ReadFile(the_file)
    content = full[0]
    content = ChangeContent(content, 'Panasonic','HyperPrint', 'regionScan','350')
    content = ChangeContent(content, 'Sony','Killjoy','price','4000')
    print(content.get('Sony'))

Main()

