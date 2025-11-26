import random

friends = input("enter names with spaces:").split()
length = len(friends)

payer = random.randint(0, length - 1)

print(f"{payer} will pay the bill this time")

