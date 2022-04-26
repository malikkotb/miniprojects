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
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to this blind auction.")
other_bidders = 'yes'
bids = {}
while other_bidders == 'yes':
    name = input("What is your name? ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    clear()
    
winner = ""
current_max_bid = 0
for person in bids:
    if bids[person] > current_max_bid:
        winner = person
        current_max_bid = bids[person] 

print(f"{winner} has won the auction with a bid of {current_max_bid}. Bye!")
print(bids)