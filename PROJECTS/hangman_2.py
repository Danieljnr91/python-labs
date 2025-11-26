import random


words = [
"apple", "shadow", "crystal", "puzzle", "lantern", "whisper", "voyage", "thunder", "dragon", "galaxy",
"harmony", "avalanche", "beacon", "cactus", "eclipse", "falcon", "glacier", "horizon", "insect", "jaguar",
"kingdom", "labyrinth", "meadow", "nebula", "orchid", "pirate", "quartz", "raven", "serpent", "tornado",
"umbrella", "volcano", "warrior", "zephyr", "anchor", "balloon", "canyon", "dagger", "ember", "fossil",
"goblin", "helmet", "iguana", "jigsaw", "kettle", "meteor", "nomad", "octopus", "potion", "ripple",
"saddle", "temple", "unicorn", "velvet", "willow", "xenon", "yonder", "zodiac", "acorn", "bamboo",
"cavern", "drizzle", "frost", "geyser", "harbor", "island", "jungle", "kernel", "legend", "maple",
"nectar", "olive", "pebble", "quarry", "rocket", "silver", "talon", "usher", "vortex", "walnut",
"xylophone", "yarn", "breeze", "envoy", "fabric", "gravel", "hinge", "inferno", "jester", "knuckle",
"lotus", "magnet", "nimble", "outlaw", "acorn", "ballad", "cobble", "doodle", "elm", "feather",
"goblet", "harvest", "ivory", "jungle", "kitchen", "lantern", "marble", "nectar", "oasis", "pioneer",
"quill", "resin", "sprout", "tulip", "umbrella", "valley", "whistle", "xylophone", "yacht", "zephyr",
"apricot", "broccoli", "cantaloupe", "daisy", "eggplant", "fig", "grape", "hazel", "iris", "jalapeno",
"kale", "lemon", "mango", "nectarine", "okra", "papaya", "quince", "radish", "spinach", "tomato",
"ugli", "vanilla", "watermelon", "xigua", "yam", "zucchini", "antelope", "buffalo", "cheetah", "dolphin",
"elephant", "flamingo", "gorilla", "hippopotamus", "impala", "jaguar", "kangaroo", "lemur", "moose", "narwhal",
"orangutan", "penguin", "quokka", "raccoon", "squirrel", "tortoise", "uakari", "vulture", "walrus", "xerus",
"yak", "zebra", "alphabet", "backpack", "calculator", "dictionary", "envelope", "flashlight", "glasses", "headphones", "internet",
"jacket", "keyboard", "laptop", "microphone", "notebook", "octagon", "pencil", "quartz", "refrigerator", "stapler",
"television", "umbrella", "vacuum", "wallet", "xylophone", "yogurt", "zipper", "avocado", "blueberry", "cucumber",
"donut", "eclair", "fajita", "gnocchi", "hamburger", "icecream", "jambalaya", "kebab", "lasagna", "muffin",
"nachos", "omelette", "pancake", "quiche", "risotto", "sushi", "taco", "udon", "vichyssoise", "waffle",
"xiao", "yogurt", "ziti", "architect", "biologist", "chemist", "dentist", "engineer", "farmer", "geologist", "historian",
"illustrator", "journalist", "king", "lawyer", "musician", "nurse", "officer", "pilot", "queen", "researcher",
"scientist", "teacher", "umpire", "veterinarian", "writer", "xenobiologist", "yogi", "zoologist", "airplane", "bicycle",
"caravan", "dirtbike", "excavator", "ferry", "gondola", "helicopter", "icebreaker", "jet", "kayak", "limousine",
"motorcycle", "yacht", "submarine", "truck", "unicycle", "van", "wagon", "zeppelin", "apartment", "bungalow",
"cottage", "dormitory", "estate", "farmhouse", "garage", "hotel", "igloo", "jail", "kiosk", "lighthouse",
"mansion", "novel", "office", "palace", "quonset", "residence", "shack", "temple", "utopia", "villa",
"warehouse", "xanadu", "yurt", "zendo", "acrobat", "bard", "chef", "dancer", "entertainer", "fencer",
"gambler", "hunter", "inventor", "joker", "knight", "lion", "magician", "navigator", "orator", "painter",
"quarterback", "ranger", "samurai", "trader", "umpire", "vocalist", "wizard", "xenon", "yodeler", "zenmaster",
"algebra", "binary", "calculus", "decimal", "equation", "fraction", "geometry", "hypotenuse", "integral", "jigsaw",
"kilogram", "logarithm", "matrix", "number", "operand", "parabola", "quotient", "ratio", "sine", "tangent",
"unit", "variable", "vector", "wavelength", "x-axis", "y-axis", "zenith", "anchor", "beacon", "captain",
"deck", "engine", "ferry", "galley", "helm", "island", "jetty", "kayak", "lighthouse", "mast",
"navigator", "ocean", "port", "quay", "rudder", "sail", "tugboat", "vessel", "wharf", "yacht",
"zephyr", "amethyst", "bronze", "copper", "diamond", "emerald", "feldspar", "gold", "helium", "iron",
"jade", "kryptonite", "lithium", "magnetite", "nickel", "obsidian", "platinum", "quartz", "ruby", "sapphire",
"topaz", "uranium", "vanadium", "wolfram", "xenotime", "yttrium", "zircon", "accordion", "banjo", "cello",
"drum", "euphonium", "flute", "guitar", "harmonica", "instrument", "jingle", "kazoo", "lute", "marimba",
"nyckelharpa", "oboe", "piano", "quena", "recorder", "saxophone", "trombone", "ukulele", "violin", "xylophone",
"yueqin", "zurna"
]


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
    