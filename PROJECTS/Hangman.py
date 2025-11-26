import random

#the words
words =[
    "python", "galaxy", "umbrella", "notebook", "whisper",
    "crystal", "journey", "puzzle", "lantern", "forest",
    "anchor", "velvet", "magnet", "tunnel", "silver",
    "rocket", "harvest", "dragon", "orbit", "cactus",
    "quartz", "falcon", "marble", "riddle", "thunder",
    "canvas", "voyage", "ember", "citron", "hazard",
    "meteor", "gravel", "breeze", "copper", "shadow",
    "temple", "banner", "forklift", "jungle", "siren",
    "pepper", "raven", "walnut", "filter", "branch",
    "summit", "cobalt", "pillow", "goblet"
]

#hangman diagrams
hangmen = [
"""  +---+
  |   |
      |
      |
      |
      |
=========""",
"""  +---+
  |   |
  O   |
      |
      |
      |
=========""",
"""  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
"""  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
"""  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
"""  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
"""  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
]

#generating spaces
computer_select = random.choice(words)
length = len(computer_select)
counter = 0

dash_list =[]
while counter < length:
    dash_list.append("_")
    counter += 1
print(dash_list)

hangman = 0
chances = 7

while chances > 0 and "_" in dash_list:
    guess = input("Guess a letter:").lower()
    if guess in computer_select:
        for i in range(length):
            if computer_select[i] == guess:
               dash_list[i] = guess
        print(dash_list)
  
    else:
        chances -= 1
        hangman += 1

        if hangman <= len(hangmen):
            print(hangmen[hangman-1]) 
            
            

       