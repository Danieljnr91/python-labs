height=float(input("Height(m)?:"))


if height >= 1.5:
    print("You can ride, have fun! Don't scream too much")
    
    age = int(input("How old are you?:"))
    if age >= 18:
        bill = 5.00
        print("Ticket price is $5.00")
    else:
        bill = 3.00
        print("Ticket price is $3.00")
    photo = input("Do you wish to take a photo?(Y/N):")
    if photo == "Y" or photo == "y":
        bill = bill + 2.00
    print(f"Please pay ${format(bill, '.2f')}")
else :
    print("Sorry, your not eligible for this ride!")
