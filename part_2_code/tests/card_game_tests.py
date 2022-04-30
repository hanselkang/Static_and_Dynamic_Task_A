import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("heart", 3)
        self.card2 = Card("diamond", 7)
        self.card3 = Card("spades", 1)
        self.cards = [self.card1, self.card2, self.card3]

    def test_check_for_ace_false(self):
        self.assertEqual(False, CardGame.check_for_ace(self, self.card1))

    def test_check_for_ace_true(self):
        self.assertEqual(True, CardGame.check_for_ace(self, self.card3))

    def test_highest_card(self):
        self.assertEqual(self.card2, CardGame.highest_card(self,self.card1,self.card2) )
        self.assertEqual(self.card1, CardGame.highest_card(
            self, self.card3, self.card1))
        self.assertEqual(self.card2, CardGame.highest_card(
            self, self.card3, self.card2))
    
    def test_cards_total(self):
        self.assertEqual("You have a total of 11", CardGame.cards_total(self, self.cards))
