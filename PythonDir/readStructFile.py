import pickle, shelve
import sys

def open_file(file_name, mode):
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print('Невозможно открыть файл', file_name, '. Работа программы будет завершена.\n', e)
        input('\n\nНажмите Enter, чтобы выйти')
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    line = the_file.readline()
    line = line.replace('/','\n')
    return line

def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    point = next_line(the_file)
    explanation = next_line(the_file)
    return category, question, answers, correct, point, explanation

def welcome(title):
    print('\t\tДобро пожаловать в игру "Викторина"!\n')
    print('\t\t',title, '\n')

def main():
    trivia = open_file('questGame.txt', 'r')
    title = next_line(trivia)
    welcome(title)
    record = []
    score = 0
    category, question, answers, correct,point, explanation = next_block(trivia)
    name = input('Как тебя зовут, пидарюга?')
    while category:
        print(category)
        print(question)
        for i in range(4):
            print('\t',answers[i])
        answer = int(input("Ваш ответ: "))
        if answer == int(correct):
            print('\nМолочик! Признался', end=' ')
            score += int(point)
        else:
            print('\nПиздишь как дышишь! Хуй тебе в очко!', end=' ')
        print(explanation)
        print('Твой счет, Гавно:', score, '\n\n')
        category, question, answers, correct,point, explanation = next_block(trivia)
    trivia.close()
    print('Это был последний вопрос, Хуесос!')
    print('В итоге, ты насосал на ',score,'очков')


    temp = []
    s = open('recordsGame.dat', 'rb')
    try:
        record = pickle.load(s)
    except:
        print('с файлом что-то не тоэ')
    s.close()

    record.append([name,score])
    record = sorted(record, key = lambda man: man[1],reverse=True)
    record.pop()
    
    print(record)
    # for i in range(2):
    s = open('recordsGame.dat', 'wb')

    pickle.dump(record, s)
    s.close()
        
    


main()

