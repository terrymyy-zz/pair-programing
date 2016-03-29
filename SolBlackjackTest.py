from SolBlackjack import*
from Cards import*
import unittest

class TestBlackjack(unittest.TestCase):

    def testcheck_for_posnum(self):
        '''this tests checking of a desired position is taken or not'''
        blackjack = Blackjack()
        pos_for_card1 = 1
        pos_for_card2 = 21
        pos_for_card3 = 'A'

        self.assertEqual(blackjack.check_for_posnum(pos_for_card1),1)
        self.assertEqual(blackjack.check_for_posnum(pos_for_card2),0)
        self.assertRaises(ValueError, blackjack.check_for_posnum(pos_for_card3),pos_for_card3)

    def testcheck_if_available(self):
        blackjack = Blackjack()
        blackjack.blankspot_table = [1,3,5,7,9]
        blackjack.blankspot_discard = [17,19]
        pos_for_card1 = 5
        pos_for_card2 = 20

        self.assertEqual(blackjack.check_if_available(pos_for_card1),5)
        self.assertEqual(blackjack.check_if_available(pos_for_card2),-1)

    def testmove_the_card(self):
        '''this tests whether func can move a card into desired position'''
        blackjack = Blackjack()

        pos_for_card1 = 18
        pos_for_card2 = 2
        pos_for_card3 = 9
        pos_for_card4 = 13
        pos_for_card5 = 16
        card_to_move = Card('Q','H')

        blackjack.move_the_card(pos_for_card1, card_to_move)
        self.assertTrue(card_to_move in blackjack.discardlist)
        self.assertTrue(pos_for_card1 not in blackjack.blankspot_discard)
    

        blackjack.move_the_card(pos_for_card2,card_to_move)
        self.assertTrue(card_to_move in blackjack.table['row1'])
        self.assertTrue(pos_for_card2 not in blackjack.blankspot_table)

        blackjack.move_the_card(pos_for_card3,card_to_move)
        self.assertTrue(card_to_move in blackjack.table['row2'])
        self.assertTrue(pos_for_card3 not in blackjack.blankspot_table)

        blackjack.move_the_card(pos_for_card4,card_to_move)
        self.assertTrue(card_to_move in blackjack.table['row3'])
        self.assertTrue(pos_for_card4 not in blackjack.blankspot_table)

        blackjack.move_the_card(pos_for_card5,card_to_move)
        self.assertTrue(card_to_move in blackjack.table['row4'])
        self.assertTrue(pos_for_card5 not in blackjack.blankspot_table)
    
    def testget_index(self):
        '''This tests whether func can get index of a position in the dictionary'''
        blackjack = Blackjack()
        pos_for_card1 = 1
        pos_for_card2 = 7
        pos_for_card3 = 12
        pos_for_card4 = 16
        pos_for_card5 = 19
        self.assertEqual(blackjack.get_index(pos_for_card1), ['row1',0])
        self.assertEqual(blackjack.get_index(pos_for_card2),['row2',1])
        self.assertEqual(blackjack.get_index(pos_for_card3),['row3',1])
        self.assertEqual(blackjack.get_index(pos_for_card4),['row4',2])
        self.assertEqual(blackjack.get_index(pos_for_card5),[])
    
    def testscore_a_hand(self):
        '''this test the score of a hand'''
        blackjack = Blackjack()

        list_of_cardvalue1 = [1,10]
        list_of_cardvalue2 = [1,5,5]
        list_of_cardvalue3 = [9,10,8]
        list_of_cardvalue4 = [2,3,4,6]
        list_of_cardvalue5 = [2,4,6,5]
        list_of_cardvalue6 = [3,4,1,10]
        list_of_cardvalue7 = [1,3,3,2]
        list_of_cardvalue8 = [1,1]
        list_of_cardvalue9 = [1,3,4,2]
        
        self.assertEqual(blackjack.score_a_hand(list_of_cardvalue1),10)

        
        self.assertEqual(blackjack.score_a_hand(list_of_cardvalue2),7)
        self.assertEqual(blackjack.score_a_hand(list_of_cardvalue3),0)
        self.assertEqual(blackjack.score_a_hand(list_of_cardvalue4),1)
        self.assertEqual(blackjack.score_a_hand(list_of_cardvalue5),2)
        self.assertEqual(blackjack.score_a_hand(list_of_cardvalue6),3)
        self.assertEqual(blackjack.score_a_hand(list_of_cardvalue7),4)
        self.assertEqual(blackjack.score_a_hand(list_of_cardvalue8),1)
        self.assertEqual(blackjack.score_a_hand(list_of_cardvalue9),5)
        
        
    def testscore(self):
        '''this test the game score of all hands'''
        blackjack1 = Blackjack()
        row1 = [Card('A','C'),Card('6','C'),Card('8','H'),Card('5','S'),Card('A','S')] 
        row2 = [Card('A','D'),Card('2','S'),Card('5','H'),Card('4','S'),Card('K','H')]
        row3 = [Card('9','H'),Card('10','S'),Card('K','S')]
        row4 = [Card('3','S'),Card('8','C'),Card('9','C')]
        blackjack1.table = {'row1': row1, 'row2': row2, 'row3': row3, 'row4': row4}
        self.assertTrue(blackjack1.score() == 28)

        blackjack2 = Blackjack()
        row1 = [Card('Q','D'),Card('5','H'),Card('A','D'),Card('4','S'),Card('4','H')]
        row2 = [Card('Q','C'),Card('4','S'),Card('2','H'),Card('2','C'),Card('3','D')]
        row3 = [Card('2','S'),Card('10','S'),Card('7','C')]
        row4 = [Card('10','S'),Card('7','S'),Card('3','C')]
        blackjack2.table = {'row1': row1, 'row2': row2, 'row3': row3, 'row4': row4}
        self.assertTrue(blackjack2.score() == 35)

        blackjack3 = Blackjack()
        row1 = [Card('10','S'),Card('2','S'),Card('2','C'),Card('4','C'),Card('A','H')] 
        row2 = [Card('A','D'),Card('3','S'),Card('6','C'),Card('A','S'),Card('J','S')]
        row3 = [Card('9','D'),Card('4','H'),Card('8','S')]
        row4 = [Card('7','S'),Card('7','H'),Card('7','D')]
        blackjack3.table = {'row1': row1, 'row2': row2, 'row3': row3, 'row4': row4}
        self.assertTrue(blackjack3.score() == 61)

        blackjack4 = Blackjack()
        row1 = [Card('2','H'), Card('Q','D'), Card('A','0'), Card('4','S'), Card('3','S')] 
        row2 = [Card('4','H'), Card('A','H'), Card('8','D'), Card('9','H'), Card('A','C')]
        row3 = [Card('J','C'), Card('8','C'), Card('A','0')]
        row4 = [Card('J','H'), Card('3','D'), Card('2','S')]
        blackjack4.table = {'row1': row1, 'row2': row2, 'row3': row3, 'row4': row4}
        self.assertTrue(blackjack4.score() == 18)

        blackjack5 = Blackjack()
        row1 =  [Card('3','S'), Card('9','C'), Card('8','C'), Card('7','S'), Card('5','S')]
        row2 =  [Card('6','C'), Card('10','D'), Card('8','D'), Card('10','D'), Card('8','S')]
        row3 =  [Card('7','C'), Card('5','C'), Card('7','H')]
        row4 =  [Card('2','C'), Card('10','D'), Card('A','C')]
        blackjack5.table = {'row1': row1, 'row2': row2, 'row3': row3, 'row4': row4}
        self.assertTrue(blackjack5.score() == 7)

      

if __name__ == '__main__':
    unittest.main()



