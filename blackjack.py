import random
from os import system, name
from time import sleep
def clear():
    # windows
    if name == 'nt':
        _ = system('cls')
    # unix (here os.name is 'posix')
    else:
        _ = system('clear')
    
clear()
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

""" 
Rules of Blackjack / 21:
Goal: add up cards to largest nr. without going over 21
- if cards in ur hand add up to more than 21 -> Bust -> u lose
- Cards from 2 to 10 count as their face value; but Jack, Queen, King count as 10; Ace can count as 1 or 11
- depending on wether you've gone over 21 or under 21 u can decide which value the Ace should represent

Example game:
- Dealers first card: 10 
- Your first card: Queen (also 10 as value)

Then dealer deals a second card to each of you

- Dealers second hand is concealed -> so u cant workout what their total is
- Your second hand is a 3

So Dealer has 10 + ? 
You have 10 + 3 = 13

You can then ask the dealer for a 3rd card 

You're lucky and you get a 7 -> total = 20 
(But if you're unlucky and you get a 10 -> total = 23 -> you lose)

Now @ this point you can say you don't want any more cards and the dealer reveals his second hand

Dealers second hand is a 10 
-> Dealers total = 20 
==> Draw

Dealers second hand is an Ace -> interpreted as 11 -> total = 21 
=> you lose

Dealers second hand is a 2 -> total = 12
!! Now in this case the dealer has to pick another card bevause his total was <17
"""

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(logo)
play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")

while play == 'y':
    user_cards = random.choices(cards, k=2)
    computer_cards = random.choices(cards, k=2)
    print(f"Your cards: {user_cards}")
    print(f"Dealer's first card: {computer_cards[0]}")
    third_card = input("Type 'y' to get another card, type 'n' to pass: ")# 'y' for another card, 'n' to pass
    if third_card == 'y':
        user_cards.append(random.choice(cards))
    
    user_total = sum(user_cards)
    dealer_total = sum(computer_cards)
    if dealer_total < 17:
        computer_cards.append(random.choice(cards))
        dealer_total = sum(computer_cards)
    
    print(f"Your final hand: {user_cards} -> total = {user_total}")
    print(f"Dealer's final hand: {computer_cards} -> total = {dealer_total}")
    if user_total < dealer_total:
        print("You win")
    elif user_total == dealer_total:
        print("Draw")
    elif user_total > dealer_total and user_total <= 21:
        print("You win")
    else:
        print("You lose")

    play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
    if play == 'y':
        clear()
