import random
def Hello():
    '''Приветствие'''
    print('Здравствуйте! Вы попали в игру "Отгадай число"')

def ask_number():
    number = int(input('Наберите число от 1 до 100\t'))
    return number

def low_high(number,computer):
    '''Функция определяет больше и меньше заданное пользователем число'''
    if number < computer:
        print('Загаданное число больше вашего числа')
    elif number > computer:
        print('Загаданное число меньше вашего числа')

def random_number():
    computer = random.randint(1,100)
    return computer 

def winner(computer):
    number = None
    while number != computer:
        number = ask_number()
        low_high(number, computer)
    print('Поздравляю! Вы отгадали число')

def main():
    Hello()
    computer = random_number()
    winner(computer)

main()
