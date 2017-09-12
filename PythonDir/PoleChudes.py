import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import random

#ИГРА "ПОЛЕ ЧУДЕС"
#Сначала парсим страницу и находим слова
#кладем все слова в список
#выбираем рандомно одно слово

url = 'parsingPage.html'

html = open(url).read()
soup = BeautifulSoup(html, 'html.parser')

regexp = r'([a-zA-Z]+)'
re2 = r'[а-яА-Я]{2,15}'
sdf = soup.find_all('p', text=re.compile(regexp))
lst = re.findall(re2, str(sdf))

word = random.choice(lst)
hideword = '_'*len(word)

#Игра начинается

print('Добро пожаловать в ПОЛЕ ЧУДЕС!')
print('\nОт вас требуется отгадать слово! У вас три попытки\nназвать и пять попыток назвать букву из слова!')
print('\nИТАК, НАЧИНАААААААЕМ!!!')
print('\nУ слова ', len(word), 'букв')

usr = ''
popword = 3
popletter = 5

while popword != 0:
    print('У вас ', popword, 'попыток назвать слово и ', popletter, 'попыток назвать букву')
    print('Ваше слово - ', hideword)
    print('Желаете назвать слово целиком и отгадать букву?')

    chs = input('1 - назвать слово\t2 - отгадать букву\t3 - Выйти из игры  ')
    if chs == '1':
        usrword = input('Напишите слово целиком\n\t')
        if usrword.lower() == word.lower():
            print('''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                ВЫ ОТГАДАЛИ СЛОВО
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!''')
            break
        else:
            print('Вы назвали неправильное слово!')
            popword -= 1
    if chs == '2':
        usrletter = input('Напишите букву\t')
        while usrletter in hideword:
            print('Эту букву вы уже называли')
            usrletter = input('Напишите другую букву ')
        if usrletter.lower() in word.lower():
            print('ВЫ ОТГАДАЛИ БУКВУ!')
            new = ''
            for i in range(len(word)):
                if word[i].lower() == usrletter.lower():
                    new += word[i]

                else:
                    #НЕ ДОДЕЛАЛ: ОСТАВИТЬ БУКВЫ В СКРЫТОМ СЛОВЕ!
                    new += hideword[i]
            hideword = new
            popletter -= 1

        else:
            print('буквы нет в слове')
            popletter -= 1
             
    if chs == '3':
        print('Вы решили выйти из игры')
        break
if popword == 0: 
    print('Вы истратили все свои попытки')
    print('''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                  GAME OVER
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!''')
