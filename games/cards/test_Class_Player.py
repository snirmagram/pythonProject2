from unittest import TestCase
from games.cards.Class_Player import Player
from games.cards.Class_DeckOfCard import DeckOfCards
from games.cards.Class_card import Card

class TestPlayer(TestCase):
    def setUp(self):
        self.player1=Player("ori",DeckOfCards(),26)
        self.deck1=DeckOfCards

    def test_set_hand(self):
        self.player2=Player("snir",DeckOfCards(),30)
        self.player3=Player("roie",DeckOfCards(),0)
        self.player4=Player("itay",DeckOfCards(),-4)

        self.assertEqual(self.player2.pack,26)
        self.assertEqual(self.player3.pack,0)
        self.assertEqual(self.player4.pack,-4)


    def test_get_card(self):
        self.assertNotIn(self.player1.get_card(),self.player1.hand())

    def test_add_card(self):
        #self.add= self.player1.add_card(self)
        self.card =Card(10,4)
        yad = self.player1.hand.copy()
        self.player1.add_card(self.card)

        self.assertNotEqual(self.player1.hand,yad)

    def test_show(self):
        pass
