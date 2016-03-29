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
        #correct the code below
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
        '''raise NotImplementedError'''
    def deal(self):
        # get the last card in the deck
        # simulates a pile of cards and getting the top one
        return self.__deck.pop()
        '''raise NotImplementedError'''   
    def __str__(self):
        """Represent the whole deck as a string for printing -- very useful during code development"""
        #the deck is a list of cards
        #this function just calls str(card) for each card in list
        deck = ''
        for card in self.__deck:
            deck += card.__str__() + '\n'
        return deck
import Cards
class Blackjack():
    def __init__(self):
        '''initialize a Blackjack game'''
        self.table             = {}
        self.table['row1']     = range(1,6)
        self.table['row2']     = range(6,11)
        self.table['row3']     = range(11,14)
        self.table['row4']     = range(14,17)
        self.discardlist       = range(17,21)
        self.blankspot_table   = range(1,17)
        self.blankspot_discard = range(17,21)
    def check_for_posnum(self,pos_for_card):
        '''this functions checks if the player's input is valid'''
        while pos_for_card not in range(1,21):
            pos_for_card = input('The position you just entered is not appropriate,pleas enter another one\n')
        return pos_for_card
    def check_if_available(self,pos_for_card):
        ''' this functions checks if the position for the new card is taken'''
        while pos_for_card not in self.blankspot_table and pos_for_card not in self.blankspot_discard:
            pos_for_card = input('The position is already taken, please enter another one\n')
        return pos_for_card
    def move_the_card(self, pos_for_card, card_to_move):
        '''this functions moves the new card to the desired spot'''
        if pos_for_card in range(17,21):
            index_for_card = self.discardlist.index(pos_for_card)
            self.discardlist[index_for_card] = card_to_move
            self.blankspot_discard.remove(pos_for_card)
        else:
            index_for_card = self.get_index(pos_for_card)
            self.table[index_for_card[0]][index_for_card[1]] = card_to_move
            self.blankspot_table.remove(pos_for_card)
    def get_index(self,pos_for_card):
        '''this functions gets the index of the card in table based on position'''
        index_for_card = []
        for row in ['row1','row2','row3','row4']:
            for item in self.table[row]:
                if item == pos_for_card:
                    index_for_card = [row,self.table[row].index(item)]
        return index_for_card
    def display_status_quo(self):
        ''' this function displays the current status of the game'''
        for key in self.table:
            print ','.join(str(x) for x in self.table.get(key))
        print 'The discrd pile is ', ','.join(str(x) for x in self.discardlist)
    def score_a_hand(self,list_of_cardvalue):
        ''' this function calculates the score for a row or a column'''
        score = 0
        score_to_point = {21:[7,10],20:[5],19:[4],18:[3],17:[2],16:[1],22:[0]}
        score = sum(list_of_cardvalue)
        if 1 in list_of_cardvalue and score < 21:
            if score + 10 < 22:
                score += 10
        if score < 17:
            score = 16
        elif score > 21:
            score = 22
        if len(list_of_cardvalue) == 2 and score == 21:
            points = score_to_point[score][1]
        else:
            points = score_to_point[score][0]
        return points
    def score(self):
        ''' this function calculates the final score'''
        score = 0
        row1, row2, row3, row4 = [[],[],[],[]]
        value_array = [row1, row2, row3, row4]
        i = 0
        for key in self.table:
            for card in self.table[key]:
                value_array[i].append(card.get_value())
            i += 1
        column1 = [row1[0],row2[0]]
        column2 = [row1[1],row2[1],row3[0],row4[0]]
        column3 = [row1[2],row2[2],row3[1],row4[1]]
        column4 = [row1[3],row2[3],row3[2],row4[2]]
        column5 = [row1[-1],row2[-1]]
        scorelist = [row1,row2,row3,row4,column1,column2,column3,column4,column5]
        for elem in scorelist:
            score += self.score_a_hand(elem)
        return score
    def play(self):

        new_deck = Deck()
        new_deck.shuffle()
        display_status_quo(self)
        dealt_card = new_deck.deal()
        print 'the new card from the deck is ', dealt_card

        while blankspot_table != []:
            pos_for_card = raw_input('Which spot do you want to put this card?\n')
            pos_for_card = self.check_if_available(self,pos_for_card)
            pos_for_card = self.check_for_posnum(self.pos_for_card)
            self.move_the_card(self,pos_for_card,dealt_card)
            display_status_quo(self)
            dealt_card = new_deck.deal()
            print 'the new card from the deck is ', dealt_card

        print 'all 16 points of the tableau are filled, the score is \n'

        score = self.socre()

        print 'The score is ', score
        
def main():
    new_deck = Deck()
    a = [0,0,0,0,0,0,0]
    for index in range(1,10000):
        newBlackjack = Blackjack()
        new_deck.shuffle()

        for i in range(1,21):
            newBlackjack.move_the_card(i,new_deck.get_deck()[i])

        print newBlackjack.score()
        # newBlackjack.display_status_quo()
    	if newBlackjack.score() > 30 :
    		a[0] += 1
    	elif newBlackjack.score() <= 30 and newBlackjack.score() >25:
    		a[1] += 1
    	elif newBlackjack.score() <= 25 and newBlackjack.score() >20:
    		a[2] += 1
    	elif newBlackjack.score() <= 20 and newBlackjack.score() >15:
    		a[3] += 1
    	elif newBlackjack.score() <= 15 and newBlackjack.score() >10:
    		a[4] += 1
    	elif newBlackjack.score() <= 10 and newBlackjack.score() >5:
    		a[5] += 1
    	elif newBlackjack.score() <= 5 and newBlackjack.score() >0:
    		a[6] += 1

    print a

if __name__ == '__main__':
    main()
