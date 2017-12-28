import os
import codecs
def OpenFile(file_name, mod):
    try:
        the_file = codecs.open(file_name, mod,encoding='utf-8',errors='ignore')
    except IOError as e:
        print('Невозможно открыть файл - ',file_name,'. Работа программы будет завершена. \n', e)
    else:
        return the_file

def Main():
    for filename in os.listdir(os.getcwd()):
        the_file = OpenFile(filename,'r')
        print('New File: ', filename,'\n',the_file.read())

Main()

