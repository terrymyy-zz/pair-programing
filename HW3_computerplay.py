import random
global deck, discard
deck  =  list(range(1,61))
discard = list()
             
def shuffle():
    global deck, discard
    if len(deck) == 0:
        discard.shuffle()
    else:
        deck.shuffle()

def check_racko(rack):
    return sorted(rack, reverse =  True) == rack

def deal_card():
    global deck
    new_card = deck.pop()
    return new_card

def deal_initial_hands():
    global deck
    computer_hand = list()
    user_hand = list()
    for i in range(0,10):
        computer_hand.append(deal_card())
        user_hand.append(deal_card())
    return computer_hand, user_hand

def does_user_begin():
    ''' user begins if 1 pops up, computer begins if 0 pops up'''
    return random.randint(0,1) == 1

def print_top_to_bottom(rack):
    for card in rack:
        print card

def find_and_replace(newCard,cardToBeReplaced,hand):
    global deck, discard
    index = hand.index(cardToBeReplaced) 
    if index in range(0,10):
        hand[index] = newCard
        add_card_to_discard(cardToBeReplaced)
    else:
        print ' Sorry the card you wanna replace is not actually in your hand'
    return hand 

def add_card_to_discard(card):
    global discard
    discard.append(card)

def computer_play(hand):
    global deck,discard
    # find the most resonable position for the first card from the discard
    card_discard = discard[-1]
    pos1 = (60 - card_discard) / 6
    if (60-hand[pos1])/6 == pos1:
        if hand(pos1) > card_discard:
            if (pos1+1 <= 9) and (60 - hand(pos1+1))/6 != pos1 +1:
                card_discard = discard.pop()
                hand = find_and_replace(card_discard,hand(pos1+1),hand)
            else:
                gotodeck = 1
        else:
            if (pos1 - 1)>= 0 and (60 - hand(pos1-1))/6 != pos1 - 1:
                card_discard = discard.pop()
                hand = find_and_replace(card_discard,hand(pos1-1),hand)
            else:
                gotodeck = 1
    else:
        card_discard = discard.pop()
        hand = find_and_replace(card_discard,hand(pos1+1),hand)

    if gotodeck == 1:
        card_deck = deck.pop()
        pos2 = (60 - card_deck) / 6
        if (60-hand(pos2)/6 == pos2:
            if hand(pos2) > card_deck:
                if (pos2+1 <= 9) and (60 - hand(pos2+1))/6 != pos2 +1:
                    hand = find_and_replace(card_deck,hand(pos2+1),hand)
            else:
                if (pos2 - 1)>= 0 and (60 - hand(pos2-1))/6 != pos2 - 1:
                    hand = find_and_replace(card_deck,hand(pos2-1),hand)
        else:
            add_card_to_discard(card_deck)
    return hand




    if card_discard > hand(pos1):
        find_and_replace(card_discard,hand(pos1),hand)
    elif pos2 < 10 and card_discard > hand(pos2):
        find_and_replace(card_discard,hand(pos2),hand)
    else:
        card_deck = deck.pop()
        pos3 = card_deck / 6
        pos4 = pos3 + 1
        if card_deck > hand(pos3):
            find_and_replace(card_deck,hand(pos3),hand))
        elif pos4 < 10 and card_deck > hand(pos4)
            find_and_replace(card_deck,hand(pos4),hand)
        else:
            add_card_to_discard(card_deck)
    return hand


def main():
    global deck,discard
    shuffle()
    computer_hand,use_hand = deal_initial_hands()
    userStarts = does_user_begin()
    print_top_to_bottom(user_hand)
    add_card_to_discard(deck.pop())
    while (not check_racko(user_hand)) and (not check_racko(computer_hand)):
        computer_hand = computer_play(computer_hand)
        user_choice = raw_input('Do you want this card?, y/n \n')
        print_top_to_bottom(user_hand)
        if user_choice == 'y':
            card_to_replace = raw_input('Which card do you wanna replace?\n')
            user_hand = find_and_replace(card,card_to_replace,user_hand)
            print_top_to_bottom(user_hand)
            elif user_choice == 'n':
                card = deck.pop()
                print 'The card you get from the deck is ' + str(card)
                secondChoice = raw_input('Do you wanna keep this card?\n')
                if secondChoice == 'y':
                    card_to_replace = raw_input('Which card do you wanna replace?\n')
                    user_hand = find_and_replace(card,card_to_replace,user_hand)
                else:
                    discard.append(card)
                    print_top_to_bottom(user_hand)
        if len(deck) == 0:
            shuffle()
                    
        
            
        
    
    
    
        

        
    
    
    
