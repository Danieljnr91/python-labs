import random
from boyp import *



computer_choice = random.choice(words)
length = len(computer_choice)

counter = 0
dash_list = []
while counter < length:
    dash_list.append("_")
    counter += 1
print(dash_list)

hangman = 0
chances = 7
while chances > 0 and "_" in dash_list:
    guess = input("Choose a letter:").lower()
    if guess in computer_choice:
        for i in range(length):
            if computer_choice[i] == guess:
                dash_list[i] = guess
        print(dash_list)
        
    
        
    elif guess not in computer_choice:
        chances -= 1
        print(f"You have {chances} chances left")
        hangman += 1
        if hangman <= len(hangmen):
          print(hangmen[hangman-1])
        
if "_" not in dash_list:
    print(f"You've won!! {computer_choice} that was it!")
else:
    print("Better luck next time")
    print("The word was... ")
    print(computer_choice)
    