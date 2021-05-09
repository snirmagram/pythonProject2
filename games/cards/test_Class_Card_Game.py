from unittest import TestCase

import games.cards.Class_Player
from games.cards.Class_Card_Game import Card_Game
from games.cards.Class_Player import Player
from games.cards.Class_DeckOfCard import DeckOfCards

class TestCard_Game(TestCase):
    def setup(self):
        self.game1 = Card_Game("ori", "snir", 15)
        self.player1 = Player("ori",DeckOfCards,15)
        self.player2 = Player("snir",DeckOfCards,15)

    def test_new_game(self):
        pass

    def test_get_winner(self):
        self.player1 = Player("ori", DeckOfCards, 15)
        self.player2 = Player("snir", DeckOfCards, 15)
        self.assertTrue(len(self.player1.hand) == len(self.player2.hand))

