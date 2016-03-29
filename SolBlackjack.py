from Cards import *

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
        try:
            if int(pos_for_card) not in range(1,21):
                return 0
            elif int(pos_for_card) in range(1,21):
                return pos_for_card
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."
        
    def check_if_available(self,pos_for_card):
        ''' this functions checks if the position for the new card is taken'''
        if pos_for_card not in self.blankspot_table and pos_for_card not in self.blankspot_discard:
            return -1
        else:
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
        print '*'*40+'\nBlackjack Table:\n'
        for key in self.table:
            if key in ['row3','row4']:
                print '\t'+'\t'.join(str(x) for x in self.table.get(key))
            else:
                print '\t'.join(str(x) for x in self.table.get(key))
        print '\nDiscard Pile:\n', '\t'.join(str(x) for x in self.discardlist)
        print '*'*40+'\n'

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

        blackjack = Blackjack()
        new_deck = Deck()
        new_deck.shuffle()
        blackjack.display_status_quo()
        pos_for_card = 0

        while blackjack.blankspot_table != []:
            dealt_card = new_deck.deal()
            print 'You have a new card!\t', dealt_card
            pos_for_card = input('Where do you want to put this card?\n')
            while blackjack.check_for_posnum(pos_for_card) == 0 :
                pos_for_card = input('Sorry we only have position 1~20! ;(\n')
            while blackjack.check_if_available(pos_for_card) == -1:
                pos_for_card = input('That position is already taken, please change another position :P\n')
            blackjack.move_the_card(pos_for_card,dealt_card)
            blackjack.display_status_quo()

        print '$'*50+'\nMission completed!!!'
        print 'All 16 spots of the tableau have been filled.'
        print 'Wonder what you score is?\n'+'$'*50

        score = blackjack.score()

        print 'Your score is ...', score, '!!!\n'

        f = open('highScore.txt')
        highScore = f.readlines()
        if score > int(highScore[0]):
            print '#'*15+'Congratulations!!!'+'#'*15
            print 'You break the highScore record!!!'
            print 'You are now awarded as master of Blackjack!!!\n'+'#'*48
        f.close()

def main():
    bj_solitaire = Blackjack()
    bj_solitaire.play()




if __name__ == '__main__':
    main()