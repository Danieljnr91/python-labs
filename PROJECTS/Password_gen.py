import random
print("PASSWORD GENERATOR")

#DATA ARRAY
letters = ['A','b','C','D','E','F','G','H','i','j','k','l','n','M','N','O','P','Q','R','S','T','U','v','w','x','y','z']

symbols = ['#','$','&','?','/','!','%','|','+','@']

numbers = [0,1,2,3,4,5,6,7,8,9]

#USER INPUT
letter_choice = int(input("How many letters do you want?:"))

symbol_choice = int(input("How many symbols do you want?:"))

number_choice = int(input("How many numbers do u want?:"))

#RANDOMISATION
letter_random = random.choices(letters, k=letter_choice)

symbol_random = random.choices(symbols, k=symbol_choice)

number_random = random.choices(numbers, k=number_choice)

#CONCATENATION
letter_conc = "".join(letter_random)

symbol_conc = "".join(symbol_random)

number_conc = "".join(str(i) for i in number_random)

#OUTPUT
raw_output = letter_random + symbol_random + number_random
random.shuffle(raw_output)
final_output = "".join(str(i) for i in raw_output)

print(f"Your Password is {final_output}")