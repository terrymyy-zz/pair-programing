import random
global deck, discard
deck    =  list(range(1,61))
discard =  list()
             
def shuffle():
    #shuffle the deck or the dicard pile by checking the length of the deck
    global deck, discard
    if len(deck) == 0:
        random.shuffle(discard)
    else:
        random.shuffle(deck)

def check_racko(rack):
    #check if racko is achieved by either player
    return sorted(rack, reverse =  True) == rack

def deal_card():
    global deck
    new_card = deck.pop()
    return new_card

def deal_initial_hands():
    global deck
    computer_hand = list()
    user_hand     = list()
    for i in range(0,10):
        computer_hand.append(deal_card())
        user_hand.append(deal_card())
    return computer_hand, user_hand

def does_user_begin():
    #user begins if 1 pops up, computer begins if 0 pops up
    if random.randint(0,1) == 1:
        print "User first!!"
    else:
        print "Computer first!!"
    return random.randint(0,1) == 1

def print_top_to_bottom(rack):
    print "Your card in hand is as follows:"
    for card in rack:
        print card
        
def print_top_to_bottom_com(rack):
    print "Computer's card in hand is as follows:"
    for card in rack:
        print card
        
def find_and_replace(newCard,card_to_replace,hand):
    global deck, discard
    while card_to_replace not in hand:
        print ' Sorry the card you wanna replace is not actually in your hand'
        card_to_replace = input('Which card do you wanna replace?\n')
        
    index = hand.index(card_to_replace)
    hand[index] = newCard
    add_card_to_discard(card_to_replace)
    return hand

def add_card_to_discard(card):
    global discard
    discard.append(card)

def computer_play(hand):
    global deck,discard
    gotodeck = False
    '''
       Find the most resonable position for the first card from the discard. In this strategy, every card, from 1 to 60
       is assigned a ideal position(slot) to  maximazize the odd to achieve Racko. For instance, 1 is supposed to be in 
       slot 10 and 60 is supposed to be in slot 1. The computer decides whether to accept or discard by the following process:
       1) Find the most proper position for the card
       2) See if the card,which is in that position currently, fits the position.
          if not: replace that card using the new card.
          if yes: determine if the new card can be place in the adjacent postion. 
                  if the new card cannot be place in the adjacent position, discard it.
    '''



    card_discard = discard[-1]
    pos1 = (60 - card_discard) / 6
    # find the ideal position for the card_discard
    if (60-hand[pos1])/6 == pos1:
    # determine if card at pos1 really fits the position
        if hand[pos1] > card_discard:
            if (pos1+1 <= 9) and (60 - hand[pos1+1])/6 != pos1 +1:
                card_discard = discard.pop()
                hand = find_and_replace(card_discard,hand[pos1+1],hand)
            else:
                #give up the first card from the discard pile and check the deck
                gotodeck = True
        else:
            if (pos1 - 1)>= 0 and (60 - hand[pos1-1])/6 != pos1 - 1:
                card_discard = discard.pop()
                hand = find_and_replace(card_discard,hand[pos1-1],hand)
            else:
                gotodeck = True
    else:
        card_discard = discard.pop()
        hand = find_and_replace(card_discard,hand[pos1],hand)

    if gotodeck:
        card_deck = deck.pop()
        pos2 = (60 - card_deck) / 6
        if (60-hand[pos2])/6 == pos2:
            if hand[pos2] > card_deck and (pos2+1 <= 9) and (60 - hand[pos2+1])/6 != pos2 +1:
                    hand = find_and_replace(card_deck,hand[pos2+1],hand)
            elif hand[pos2] < card_deck and (pos2 - 1)>= 0 and (60 - hand[pos2-1])/6 != pos2 - 1:
                    hand = find_and_replace(card_deck,hand[pos2-1],hand)
            else:
                add_card_to_discard(card_deck)
        else:
            hand = find_and_replace(card_deck,hand[pos2],hand)
    return hand

def main():
    global deck,discard
    print "Welcome to the Racko Game!"
    shuffle()
    computer_hand,user_hand = deal_initial_hands()
    add_card_to_discard(deck.pop())
    user_starts             = does_user_begin()    
    while (not check_racko(user_hand)) and (not check_racko(computer_hand)):
        if user_starts == False:
            computer_play(computer_hand)
            print "Computer finish playing!"
        
        ## user begins to play
        print_top_to_bottom(user_hand)
        print "This is the discard first card: ", discard[-1]
        user_choice   = raw_input('Do you want this card?(y/n) \n')
        if user_choice == 'y':  
            card_to_replace = input('Which card do you wanna replace?\n')
            user_hand   = find_and_replace(discard[-1],card_to_replace,user_hand)
            print "Your cards has changed to the following:"
            print_top_to_bottom(user_hand)
        elif user_choice == 'n':
            card = deck.pop()
            print 'The card you get from the deck is ' + str(card)
            second_choice = raw_input('Do you wanna keep this card?(y/n)\n')
            if second_choice == 'y':
                card_to_replace = input('Which card do you wanna replace?\n')
                user_hand       = find_and_replace(card,card_to_replace,user_hand)
                print "Your cards has changed to the following:"
            else:
                print "Your cards is not changed!"
                discard.append(card)
            print_top_to_bottom(user_hand)
        
        if user_starts == True:
            computer_play(computer_hand)
            print "computer finish playing!"
            
        if len(deck) == 0:
            shuffle()


    if check_racko(user_hand):
        print "Racko! Congratulations! You win!"
    elif check_racko(computer_hand):
        print "Racko! Sorry, computer wins!"
       
if __name__ == '__main__':
    main()
