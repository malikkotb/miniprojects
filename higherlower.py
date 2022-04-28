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
logo = """
    __  ___       __                               __                          
   / / / (_____ _/ /_  ___  _____   ____  _____   / /  ____ _      _____  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/  / __ \/ ___/  / /  / __ | | /| / / _ \/ ___/
 / __  / / /_/ / / / /  __/ /     / /_/ / /     / /__/ /_/ | |/ |/ /  __/ /    
/_/ /_/_/\__, /_/ /_/\___/_/      \____/_/     /_____\____/|__/|__/\___/_/     
        /____/                                                                 
 """

vs = """
 _   _______
| | / / ___/
| |/ (__  ) 
|___/____/  
"""

instanames = ["Neymar", "Khloé Kardashian",
            "Rihanna",
            "Beyonce",
            "Lebron James",
            "Kobe Bryant RIP",
            "Michael Jordan",
            "Bushido",
            "Capital Bra",
            "Kevin Durant",
            "Will Smith"]
instastars = {"Neymar": 173000000, 
            "Khloé Kardashian": 238000000,
            "Rihanna": 150000000,
            "Beyonce": 254000000,
            "Lebron James": 119000000,
            "Kobe Bryant RIP": 20800000,
            "Michael Jordan": 23500000,
            "Bushido": 2100000,
            "Capital Bra": 4100000,
            "Kevin Durant": 12900000,
            "Will Smith": 64700000}
# make dictionary where value has insta followers;
score = 0
play = "y"
correctanswer = ''
sameChoice = 0
while play == 'y':
    clear()
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    if correctanswer != 'A' or (sameChoice > 1 and correctanswer == 'A'):
        choiceA = random.choice(instanames)
        sameChoice = 0
    else:
        sameChoice += 1
    print(f"Compare A: {choiceA}")
    print(vs)
    if correctanswer != 'B' or (sameChoice > 1 and correctanswer == 'A'):
        choiceB = random.choice(instanames)
        sameChoice = 0
    else: 
        sameChoice += 1
    print(f"Against B: {choiceB}")
    guess = input("Who has more followers? Type 'A' or 'B': ")

    if instastars[choiceB] > instastars[choiceA]:
        correctanswer = 'B'
    else:
        correctanswer = 'A'

    if guess == correctanswer:
        print("Very good, nobody cares about khloe")
        score += 1
        
    else:
        print(f"Sorry that's wrong. Final score: {score}")
        play = 'n'

