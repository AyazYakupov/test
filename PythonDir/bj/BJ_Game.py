import cards

class BJ_Card(cards.Card):
    def value(self):
        v = cards.Card.SUITS.index(self.suit) + 1

        if self.is_face_up == True:
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Hand(cards.Hand):
    def total(self):
        t = 0
        for card in self.cards:
            if card.value() != None:
                t += card.value()
        return t
    def fool(self,t):
        if t > 21:
            return True
        else: 
            return False
    def __str__(self):
        rep = super(BJ_Hand, self).__str__()
        rep += str(self.total())
        return rep

class BJ_Deck(cards.Deck):
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.addCard(BJ_Card(suit,rank))

    
def ask_yes_no(question):
    response = ''
    while response not in ('y','n'):
        response = input(question)
    return response

def number(question, low = 1, high = 5):
    number = None
    while number not in range(low,high):
        number = int(input(question))
    return number

def deck_creat():
        deck = BJ_Deck('deck')
        deck.populate()
        deck.shuffle()
        return deck


def game():
    response = ask_yes_no('Будете играть? ')
    if response == 'y':
        numb = number('Сколько будет игроков? (1-5) ')
        lst = []
        deck = deck_creat()
        for i in range(1,numb+1):
            name = input("Введите имя игрока: ")
            lst.append(name)
        for i in lst:
            i = BJ_Hand(i)
            deck.hand_up(i)
            print(i, end=' ')
            ask = None
            ask = ask_yes_no('взять еще карту? ')
            while ask != 'n':
                deck.giveCard(i)
                print(i, end=' ')
                if i.fool(i.total()) == True:
                    print('You fool')
                    break
                ask = ask_yes_no('взять еще карту? ')
            
        dealer = BJ_Hand('dealer')
        deck.hand_up(dealer)
        dealer.cards[0].flip()
        print(dealer)
    else: quit()

game()

