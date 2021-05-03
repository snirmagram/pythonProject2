from games.cards.Class_DeckOfCard import DeckOfCards
from games.cards.Class_Player import Player

class Card_Game:
    def __init__(self,gameon,player1,player2,pack=10):
        self.gameon= False
        self.deck = DeckOfCards()
        self.player1=Player(player1,self.deck,pack)
        self.player2=Player(player2,self.deck,pack)


    def new_game(self):
        if self.gameon==True:
            print(" ERORE ")

        cards= self.deck.shuffle()
        self.player1.set_hand(10,cards)
        self.player2.set_hand(10,cards)
        self.gameon=True


    def get_winner(self):
        if len(self.player1.hand)<len(self.player2.hand):
            return self.player1
        if len(self.player2.hand)<len(self.player1.hand):
            return self.player2
        if self.player1==self.player2:
            return
        else:
            return None


snir=Player
ori=Player
