import random  # needed for shuffling a Deck
global rank,suit
rank = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suit = ['S','C','H','D']
class Card(object):
    #the card has a suit which is one of 'S','C','H' or 'D'
    #the card has a rank   
    def __init__(self, r, s):
        #implement
        #where r is the rank, s is suit
        self.r = r
        self.s = s
        '''return NotImplementedError'''

    def __str__(self):
        return self.r + self.s

    def get_rank(self):
        return self.r

    def get_suit(self):
        return self.s      

    def get_value(self):
        if self.r in ['2','3','4','5','6','7','8','9','10']:
            return int(self.r) 
        elif self.r in ['J','Q','K']:
            return 10
        elif self.r == 'A':
            return 1

class Deck(object):
    """Denote a deck to play cards with"""

    def __init__(self):
        """Initialize deck as a list of all 52 cards:
           13 cards in each of 4 suits"""
        global rank,suit
        self.__deck = []
        for i in range(0,4):
            for j in range(0,13):
                new_card = Card(rank[j],suit[i])
                self.__deck.append(new_card)

    def shuffle(self):
        """Shuffle the deck"""
        return random.shuffle(self.__deck)

    def get_deck(self):
        return self.__deck
 
    def deal(self):
        '''this function deals a card'''
        return self.__deck.pop()
 
    def __str__(self):
        """Represent the whole deck as a string for printing -- very useful during code development"""
        deck = ''
        for card in self.__deck:
            deck += card.__str__() + '\n'
        return deck
