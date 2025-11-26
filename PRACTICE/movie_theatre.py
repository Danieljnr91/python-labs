print("WELCOME TO PARKINSON'S THEATRE")

photosensitive=input("Are you photosensitive(Y/N):").lower()

hearing = input('Do you have hearing problems?(Y/N):').lower()

if photosensitive == 'n' and hearing == "n":
    print("Great! Your total is $20.00")

elif photosensitive == 'y' and hearing == 'n':
    eyes=input("Please purchase these glasses to watch this show(Y/N):").lower()
    if eyes == 'y':
        print("Great! Your Total is $30.00")
    else:
        print("Alright, you can't watch this show")
elif photosensitive == 'n' and hearing == 'y':
    ears = input("Please purchase this specialised ear muffs to continue(Y/N):").lower()
    if ears ==  'y':
        print("Great! Your total is $30.00")
    else:
        print("Alright you cant watch this show")       
else:
    condition = input("Please purchase these ites to continue(Y/N):").lower()
    if condition == 'y':
        print("Great! Your total is $50.00")
    else:
        print("Your not ELIGIBLE for this show due to your conditions, sorry.")
   


      