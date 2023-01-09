import random
### BLACKJACK ###
import time
symbols = [u"\u2666", u"\u2665", u"\u2663", u"\u2660"]
numbers = ['2','3','4','5','6','7','8','9','J','Q','K','A']
# print(u"\u2666") # diamond ♦
# print(u"\u2665") # heart ♥
# print(u"\u2663") # club ♣
# print(u"\u2660") # spade ♠

def hand_sum(hand): # hand is a list of current cards
    current_sum = 0
    for i in hand:
        if i[0] == 'A':
            continue
        elif i[0] in ['K', 'J', 'Q']:
            current_sum += 10
        else:
            current_sum += int(i[0])

    for i in hand: # check this after the other cards have been summed up to determine wheter ace is 1 or 11
        if i[0] == 'A':
            if current_sum + 11 > 21:
                current_sum += 1
            else:
                current_sum += 11

    return current_sum

def option():
    hit_or_stay = input('Would you like to hit or stay? ')
    while hit_or_stay != 'hit' and hit_or_stay != 'stay':
        print('That is not a valid option.')
        hit_or_stay = input('Would you like to hit or stay? ')
    print(f'Your choice: {hit_or_stay}')  # kann entfernt werden
    return hit_or_stay

print('Welcome to Blackjack')
start_money = 500
while True:
    play_a_hand = input(f'\nYou are starting with ${start_money}. Would you like to play a hand? yes/no ')
    if play_a_hand == 'yes':
        # play
        user_bet = float(input('Place your bet: '))
        while user_bet <= 0 or user_bet > start_money:
            if user_bet <= 0:
                print('The minimum bet is $1')
                user_bet = float(input('Place your bet: '))
            elif user_bet > start_money:
                print('You dont have enough money to make that bet.')
                user_bet = int(input('Place your bet: '))
        print(f'Your bet is: {user_bet}') # kann entfernt werden

        # generate 2 random cards for user
        user_hand = [f'{random.choice(numbers)}{random.choice(symbols)}', f'{random.choice(numbers)}{random.choice(symbols)}']
        # generate random cards for computer, but only show one of them
        dealer_hand = [f'{random.choice(numbers)}{random.choice(symbols)}', f'{random.choice(numbers)}{random.choice(symbols)}']
        time.sleep(2) # just to give the sense that a hand is being delt
        print(f'Your delt hand: {user_hand[0]}, {user_hand[1]}')
        print(f'The dealers delt hand: {dealer_hand[0]}, Unknown')

        # pre check for blackjack
        if hand_sum(user_hand) == 21:
            print(f'The dealer has {[card for card in dealer_hand]}')
            print(f'Blackjack! You win ${1.5*user_bet}\n')
            start_money += 1.5*user_bet

        else:
            hit_or_stay = option()

            # Calculate the value of the cards
            while hit_or_stay == 'hit':
                user_hand.append(f'{random.choice(numbers)}{random.choice(symbols)}')
                print(f'You are delt: {user_hand[len(user_hand) - 1]}')
                print(f'You now have {[card for card in user_hand]}')
                # Calculate the users' hand here: if sum of hand is over 21 -> user immediately loses
                sum_user = hand_sum(user_hand)
                print(f'Your hand total at the moment is: {sum_user}.')
                if sum_user > 21:
                    # bust
                    print(f'Your hand value is over 21 and you lose {user_bet} :(')
                    start_money -= user_bet
                    break
                hit_or_stay = option()

            if hit_or_stay == 'stay':
                # user will not receive any more cards; dealers turn
                # hit and stay for dealer - functionality
                sum_user = hand_sum(user_hand)
                print(f'Your current sum: {sum_user}')
                print(f'The dealer has {[card for card in dealer_hand]}')
                dealer_sum = hand_sum(dealer_hand)

                while dealer_sum <= 16:  # dealer must hit
                    dealer_hand.append(f'{random.choice(numbers)}{random.choice(symbols)}')
                    print(f'The dealer hits and is delt: {dealer_hand[len(dealer_hand) - 1]}')
                    print(f'The dealer has {[card for card in dealer_hand]}')
                    dealer_sum = hand_sum(dealer_hand)
                    if dealer_sum > 21:  # dealer busts
                        print(f'The dealer busts, you win {user_bet}')
                        start_money += user_bet

                if dealer_sum > 16:  # dealer must stay
                    print('The dealer stays.')
                    if dealer_sum == 21:
                        print(f'The dealer wins. You lose {user_bet}')
                        start_money -= user_bet
                    if dealer_sum == sum_user:
                        print('You tie. Your bet was returned.')
                    elif dealer_sum > sum_user:
                        print(f'The dealer wins. You lose ${user_bet}.')
                        start_money -= user_bet
                    else:
                        print(f'You win {user_bet}')
                        start_money += user_bet

    else:
        # stop playing
        print(f'You have {start_money}. Thanks for playing BlackJack. Byee')
        break