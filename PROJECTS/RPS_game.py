import random
print("ROCK PAPER SCISSORS")

print("0 - Rock \n 1 - Paper \n 2 - Scissors")

user_choice = int(input("Whats your pick?:"))

computer_range = [0 , 1 , 2]

computer_choice = random.choice(computer_range)


if computer_choice == user_choice:
    print("Its a Draw")

elif user_choice == 0 and computer_choice == 1:
    print("You lose.")

elif user_choice == 0 and computer_choice == 2:
    print("You win!")

elif user_choice == 1 and computer_choice == 2:
    print("You lose")

elif user_choice == 2 and computer_choice == 1:
    print("You win!")
   

