class Animal():
    def __init__(self, name):
        self.name = name
        print("Ты создал зверюшку:", name)
        self.mood = 5
        
    def __str__(self):
        rep = "Это "
        rep += self.name
        return rep
    
    def play(self):
        print('Вы играете с',self.name,'и у зверюшки настроение улучшилось!')
        self.mood += 2

    def act(self):
        print(self.name, 'мурлычет: муррр муррр:)')
        self.mood -= 1

    def scratch(self, enemy):
        enemy.damage()
        self.mood = 5

    def howAreYou(self):
        if self.mood >= 4:
            print(self.name, 'рада до сраки!)))')
        elif 2 <= self.mood < 4:
            print(self.name, 'вроде чувствует себя ничего:|')
        else:
            print(self.name, 'чувствует себя хреново:((((((')
        

class Furnitur():
    def __init__(self, name, healf):
        self.name = name
        self.healf = healf
        print("Ты создал предмет мебели", name, 'с',healf,'healfpoint\'ов')
        self.status = 1

    def __str__(self):
        rep = 'Объект мебели - '
        rep += self.name + ' имеет ' + str(self.healf) + ' healfpoint\'ов'
        return rep

    def damage(self):
        self.healf -= 5
        if self.status == 1:
            if self.healf <= 0:
                print(self.name,'героически погиб')
                self.status = 0
            else:
                print(self.name,'испытал боль и его healfpoint\'ы = ',self.healf)
        else:
            print(self.name,'уже мертв:(((')

def main():
    anim1 = Animal('Кошка')

    chair = Furnitur('Кресло',15)
    print(chair)

    choice = None

    while choice != '0':
        print('''
Что сделать с зверюшкой?
        
        0. ВЫЙТИ
        1. Заставить промурлыкать!
        2. Поиграть со зверюшкой
        3. Дать расцарапать мебель 
        4. Узнать как у зверюшки дела \t
''')
        
        choice = input()
        if choice == '0':
            print('До свидания')

        elif choice == '1':
            anim1.act()

        elif choice == '2':
            anim1.play()

        elif choice == '3':
            anim1.scratch(chair)

        elif choice == '4':
            anim1.howAreYou()
    
        else:
            print('Неправильный ввод')

main()
