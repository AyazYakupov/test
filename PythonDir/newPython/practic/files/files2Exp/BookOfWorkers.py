import sys
import re

def OpenFile(file_name, mod):
    try:
        the_file = open(file_name, mod)
    except IOError as e:
        print('Невозможно открыть файл - ',file_name,'\nРабота программы будет завершена. \n', e)
        sys.exit()
    else: return the_file

    
def ReadBook(line):
    position = tuple(re.findall(r'\w+', line))
    return (position)

def Main():
    file_name = input('Введите имя файла: ')
    mod = input('Введите модификатор открытия файла (r/w/r+): ')
    the_file = OpenFile(file_name, mod)
    book = []
    for line in the_file:
        book.append(ReadBook(line))
    the_file.close()
    close = 1
    while close:
        choice = input('1 - Показать книгу\n2 - Найти имя\n3 - Выдать поиск по году\n4 - Выйти\nВыберите пункт: ')
        if choice == '1':
            Output(book)
        elif choice == '2':
            name = input('Напишите имя: ')
            Search(name,book)
        elif choice == '3':
            year = input('Напишите с какого года: ')
            FromYear(year,book)
        elif choice == '4': close = 0
        else: print('Неправильный ввод')
    return book

def Output(book):
    for position in book:
        print(position)
def Search(name, book):
    for position in book:
        if name == position[0]:
            print('Элемент найден!\n', position)
            return None
    print('Элемент не найден!')
    return None
def FromYear(year,book):
    for position in book:
        if position[2] >= year:
            print(position)
    return None
Main()
# f = open('output.txt', 'w')
# f.write(string)
# f.close()



