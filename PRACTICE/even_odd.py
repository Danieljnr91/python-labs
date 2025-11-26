number = int(input("Enter number: "))

remainder = number % 2

while True:
    if remainder == 0:
        print("It's an even number")
    else:
        print("It's an odd number")
    break
