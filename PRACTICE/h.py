import random
lists = ['jump','catch','hail','super']

selected = random.choice(lists)

length = len(selected)

counter = 0
dash_list = []

while counter < length:
    dash_list.append("_")
    counter += 1
print(dash_list)

chance = 6
while chance  > 0 and "_" in dash_list:
    guess = input("Guess a letter:")
    if guess in selected:
        for i in range(length):
           if selected[i] == guess:
              dash_list[i] = guess
        print(dash_list)    



