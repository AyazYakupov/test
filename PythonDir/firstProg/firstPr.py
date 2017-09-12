#!/usr/bin/python
import os
loop = True

while loop == True:

    print('Выберите пункт меню: ','\n','1) Создать словарь ','\n',
            '2) Показать словарь ','\n','3) Добавить слово ','\n',
            '4) Удалить слово ','\n','5) Отсортировать по алфавиту ',
            '\n','6) Выйти ','\n') 

    menu = input()

    if menu == '1':
        os.system('clear')
        a = []
        print('\n','Словар создан ')

    elif menu == '2':
        os.system('clear')
        print('\n', a)

    elif menu == '3':
        os.system('clear')
        print('\n','Напишите слово')
        a.append(input())

    elif menu == '4':
        os.system('clear')
        print('\n','Какое слово удалить? ')
        dl = int(a.index(input()))
        del a[dl]

    elif menu == '5':
        os.system('clear')
        def sortByAlphabet(inputStr):
            return inputStr[0]
        a.sort(key=sortByAlphabet)
        print('\n','Словарь отсортирован')

    elif menu == '6':
        os.system('clear')
        loop = False

    else:
        print('\n','Неправильный ввод')



