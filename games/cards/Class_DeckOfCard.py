from games.cards.Class_card import Card
from random import *


class DeckOfCards:
    def __init__(self):
        self.list1=[]
        self.deck()
        self.shuffle()

    def deck(self):
        for suit in range(1,5):
            for value in range(2,15):
                c1=Card(value,suit)
                self.list1.append(c1)



    def shuffle(self):
        shuffle(self.list1)
        d2=shuffle(self.list1)

    def deal_one(self):
        num= choice(self.list1)
        self.list1.remove(num)
        return num
        #self.list2.append(num)
        #self.list1.pop(num)

    def show(self):
        print(self.list1)


# d1=DeckOfCards()
# print()
# print(d1.list1)
