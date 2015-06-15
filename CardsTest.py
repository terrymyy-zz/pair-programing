from Cards import *
import unittest
import random
global rank,suit
rank = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suit = ['S','C','H','D']

class TestCards(unittest.TestCase):

    def setUp(self):
        r = random.choice(rank)
        s = random.choice(suit)
        self.new_card = Card(r,s)
        self.new_deck = Deck()
        self.new_deck1 = Deck()

    def test_get_rank(self):
        '''test whether the function get the rank of card'''
        self.assertEqual(self.new_card.get_rank(), self.new_card.r)
        self.assertFalse(self.new_card.get_rank() != self.new_card.r)

    def test_get_suit(self):
        '''test whether the function get the suit of card'''
        self.assertEqual(self.new_card.get_suit(), self.new_card.s)
        self.assertFalse(self.new_card.test_get_suit != self.new_card.s)

    def test_get_value(self):
        '''test whether the function get the value of card'''
        for self.new_card.r in rank:
            if self.new_card.r == 'A':
                self.assertEqual(self.new_card.get_value(), 1)
            elif self.new_card.r in ['J','Q','K']:
                self.assertEqual(self.new_card.get_value(), 10)
            else:
                self.assertEqual(self.new_card.get_value(), int(self.new_card.r))

    def test_card__str__(self):
        '''test whether the function print the card'''
        self.assertEqual(str(self.new_card), str(self.new_card.r+self.new_card.s))

    def test_shuffle(self):
        '''test whether the function shuffle the deck'''
        self.assertEqual(str(self.new_deck),str(self.new_deck1))
        self.new_deck.shuffle()
        self.assertFalse(str(self.new_deck) == str(self.new_deck1))

    def test_get_deck(self):
        '''test whether the function get the deck'''
        k = 0
        for i in range(0,4):
            for j in range(0,13):
                self.assertEqual(str(self.new_deck1.get_deck()[k]), str(rank[j])+str(suit[i]))
                k +=1

    def test_deal(self):
        '''test whether the function deal one card'''
        self.assertEqual(str(self.new_deck.deal()),'KD')

    def test_deck__str__(self):
        '''test whether the function print the deck'''
        deck = ''
        for i in range(0,4):
            for j in range(0,13):
                deck = deck+str(rank[j])+str(suit[i])+'\n'
        self.assertEqual(str(self.new_deck), deck)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)