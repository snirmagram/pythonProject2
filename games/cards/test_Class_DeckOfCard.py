from unittest import TestCase
from games.cards.Class_DeckOfCard import DeckOfCards
from games.cards.Class_card import Card
from random import choice


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck1 = DeckOfCards()

    def test_deck(self):

        self.assertEqual(len(self.deck1.list1), 52)

    def test_shuffle(self):
        self.list1 = []
        for suit in range(1, 5):
            for value in range(2, 15):
                c1 = Card(value, suit)
                self.list1.append(c1)
            self.assertNotEqual(self.list1, self.deck1.list1)

    def test_deal_one(self):
        self.list1 = []
        for suit in range(1, 5):
            for value in range(2, 15):
                c1 = Card(value, suit)
                self.list1.append(c1)
        self.assertIn(choice(self.list1), self.deck1.list1)