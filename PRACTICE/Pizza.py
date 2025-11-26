print("WELCOME TO PAPA'S PIZZA")

#PRICES
small_size = 100
medium_size = 200
large_size = 500

print("What are we craving today?:")
print("1. Small Size \n 2. Medium Size \n 3. Large Size")
pizza_size = int(input("Pizza Size?:"))

#small size
if  pizza_size == 1:
    pepperoni=input("would you like Pepperoni?(Y/N):")
    if pepperoni == 'Y' or pepperoni == 'y':
        print(f"Your pizza will cost ${small_size + 30}.00")
        cheese = input("Would you like extra cheese?(Y/N):")
        if cheese == 'Y' or cheese == 'y':
            print(f"Your pizza will cost ${small_size+50}.00") 
        else:
            print(f"Alright, Your pizza will cost ${small_size + 30}.00")
    else:
        print(f'Your pizza will cost ${small_size}.00')
           
# Medium size
elif pizza_size == 2:
    pepperoni=input("would you like Pepperoni?(Y/N):")
    if pepperoni == 'Y' or pepperoni == 'y':
        print(f"Your pizza will cost ${medium_size + 30}.00")
        cheese = input("Would you like extra cheese?(Y/N):")
        if cheese == 'Y' or cheese == 'y':
            print(f"Your pizza will cost ${medium_size+50}.00")
        else:
            print(f"Alright, Your pizza will cost ${medium_size + 30}.00")
    else:
        print(f'Your pizza will cost ${medium_size}.00')
           
#Large size
else:
    pepperoni=input("would you like Pepperoni?(Y/N):")
    if pepperoni == 'Y' or pepperoni == 'y':
        print(f"Your pizza will cost ${large_size + 30}.00")
        cheese = input("Would you like extra cheese?(Y/N):")
        if cheese == 'Y' or cheese == 'y':
            print(f"Your pizza will cost ${large_size+50}.00")    
           
        else:
            print(f"Alright, Your pizza will cost ${large_size + 30}.00")
    else:
        print(f'Your pizza will cost ${large_size}.00')
           
           



