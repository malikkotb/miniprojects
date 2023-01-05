import random
### BLACKJACK ###
import time

symbols = [u"\u2666", u"\u2665", u"\u2663", u"\u2660"]
numbers = ['2','3','4','5','6','7','8','9','J','Q','K','A']
# #### Beware: Ace can be 1 or 11
# J,Q,K are all 10
# print(u"\u2666") # diamond ♦
# print(u"\u2665") # heart ♥
# print(u"\u2663") # club ♣
# print(u"\u2660") # spade ♠

def option():
    hit_or_stay = input('Would you like to hit or stay? ')
    while hit_or_stay != 'hit' and hit_or_stay != 'stay':
        print('That is not a valid option.')
        hit_or_stay = input('Would you like to hit or stay? ')
    print(f'Your choice: {hit_or_stay}')  # kann entfernt werden
    return hit_or_stay

print('Welcome to Blackjack')
# TODO: mit tkinter -> zu einem interaktiven Spiel machen
start_money = 500
while True:
    play_a_hand = input(f'You are starting with ${start_money}. Would you like to play a hand? yes/no ')
    if play_a_hand == 'yes':
        # play
        user_bet = float(input('Place your bet: '))
        while user_bet <= 0 or user_bet > start_money:
            if user_bet <= 0:
                print('The minimum bet is $1')
                user_bet = int(input('Place your bet: '))
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

        hit_or_stay = option()

        # Calculate the value of the cards
        while hit_or_stay == 'hit':
            user_hand.append(f'{random.choice(numbers)}{random.choice(symbols)}')
            print(f'You are delt: {user_hand[len(user_hand) - 1]}')
            print(f'You now have {[card for card in user_hand]}')
            # Calculate the users' hand here: if sum of hand is over 21 -> user immediately loses
            sum_hand = 0
            for i in user_hand:
                if i[0] == 'A':
                    sum_hand += 11
                elif i[0] in ['K', 'J', 'Q']:
                    sum_hand += 11
                else:
                    sum_hand += int(i[0])
            print(f'Your hand total at the moment is: {sum_hand}.')
            hit_or_stay = option()

        # option is stay
        print('Your option must have been stay since youre here now.\n')

        # it pays 3:2 if you win
        # 3/2 * 100
        # update the start_money



    else:
        # stop playing
        break