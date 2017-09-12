class Card():
    SUITS = ('A','2','3','4','5','6','7','8','9','10','J','D','K')
    RANKS = ('c','d','h','s')
    def __init__(self, suit, rank, face_up = True):
        self.suit = suit
        self.rank = rank
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up == True:
            rep = self.suit + self.rank
        else:
            rep = 'Xx'
        return rep
    def flip(self):
        self.is_face_up = not self.is_face_up


class Hand():
    def __init__(self,name):
        self.cards = []
        self.name = name
    def __str__(self):
        rep = self.name + ': '
        for card in self.cards:
            rep += str(card) + ' '
        return rep
    def addCard(self,card):
        self.cards.append(card)
    def clear(self):
        self.cards = []

class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.addCard(Card(suit, rank))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def giveCard(self,hand):
        card = self.cards[0]
        self.cards.pop(0)
        hand.addCard(card)
    def hand_up(self,name):
        for i in range(2):
            self.giveCard(name)    



