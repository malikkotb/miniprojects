import random

words = ["banana", "apple", "octopus"]

chosen_word = random.choice(words)
uncovered_word = ""
for i in range(len(chosen_word)):
    uncovered_word += '*'
lives = len(uncovered_word) + 3
print(f"The word has been chosen, it has {len(chosen_word)} letters. You have as many lives as letters + 3 -> Lives = {lives}")
print(uncovered_word)

# a set representing the letters that the user has already chosen
chars = set()
correct_chars = set() # set representing the letters in the word
for i in range(len(chosen_word)):
    correct_chars.add(chosen_word[i])

#print(correct_chars)

user_guess = input(f"Lives = {lives}. What is your first guess? ")

for i in range(len(chosen_word)):
    if user_guess == chosen_word[i]:
        # replace string at specific position
        uncovered_word = uncovered_word[:i] + chosen_word[i] + uncovered_word[i+1:]
    
if user_guess not in chosen_word:
    lives -= 1
print(uncovered_word)

while '*' in uncovered_word and lives > 0:
    user_guess = input(f"Lives = {lives}. What is your guess? ")
    for i in range(len(chosen_word)):
        if user_guess == chosen_word[i]:
            uncovered_word = uncovered_word[:i] + chosen_word[i] + uncovered_word[i+1:]
    if user_guess not in chosen_word:
        lives -= 1
    print(uncovered_word)

if lives < 1:
        print("You're hung. Rip")
else:
    print('Yeay u got it right.')