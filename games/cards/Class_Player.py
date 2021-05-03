from random import *

from games.cards.Class_DeckOfCard import DeckOfCards

class Player:
    def __init__(self,name,cards,pack=10):
        self.name=name
        self.pack=pack
        if self.pack >26:
            self.pack=26
        self.hand=self.set_hand(self.pack,cards)

    def set_hand(self,num_of_cards,deck):
        hand=[]
        for i in range(num_of_cards):
            card=deck.deal_one()
            hand.append(card)
        return hand

    def get_card(self):
        hand=self.hand
        taken=choice(hand)
        self.hand.remove(taken)
        return self.hand


    def add_card(self):
        self.hand.append(cards2)

    def show(self):
        print(f"{self.name}:{self.hand}")


cards2=DeckOfCards()
snir=Player("snir",cards2)
print(len(snir.hand))
print(len(cards2.list1))