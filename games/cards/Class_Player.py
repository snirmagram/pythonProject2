from random import *
from games.cards.Class_DeckOfCard import DeckOfCards

class Player:
    def __init__(self,name,cards,pack=10):
        self.name=name
        self.pack=pack
        if self.pack >26:
            self.pack=26
            if self.pack < 0:
                self.pack == 0
        self.hand=self.set_hand(self.pack,cards)


    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


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
        return taken


    def add_card(self,card):
        self.hand.append(card)

    def show(self):
        print(f"{self.name}:{self.hand}")


#cards2=DeckOfCards()
#snir=Player("snir",cards2)
#print(len(snir.hand))
#print(len(cards2.list1))