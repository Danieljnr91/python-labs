import random

list1 = [1,2,3,4,5,6,7,8,9]

pass_length = int(input("password length:"))


target = [1,2,3,4,5,6,7,8,9,]
attempts = 0

while True:
    pass_list = random.choices(list1 , k = pass_length)
    random.shuffle(pass_list)
    
    attempts = attempts + 1
    print(f"Attempts {attempts} : {pass_list}")
    
    if pass_list == target:
        print("ACCESS GRANTED")
        break
    if attempts == 100000:
        print("Sorry couldnt fine password")
        break
    


