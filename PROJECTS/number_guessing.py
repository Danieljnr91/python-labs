import random

print("I'll think of a number between 1 and 50 try your best to guess that number")

computer_choice = random.randint(1,50)
print("1.Hard \n 2.Easy")
difficulty = int(input("Choose difficulty:"))

if difficulty == 1:
  chances = 5
  print("You have 5 chances to guess")
else:
  chances = 10
  print("You have 10 chances to guess")

attempts = 0

while True:
  user_guess = int(input("Guess a number:"))
  if user_guess > 50 or user_guess < 0:
     print(f"The range of numbers is 1 - 50, {user_guess} is outside that range!")

  attempts += 1

  if user_guess < computer_choice:
    chances -= 1
    print(f"Too Low! Try again, you have {chances} left")
  elif user_guess > computer_choice:
        chances -=1
        print(f"Too High! Try again, you have {chances} left")  
  else:
     print(f"BINGO! That's it! {computer_choice} it took you {attempts} attempts to figure that one out") 
  
  if chances == 0:
     print(f"Game Over, the number was {computer_choice}")
     break
