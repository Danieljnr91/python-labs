def prime_checker(number):
    if number <= 1:
        print(f"{number} is not a prime number")
    for i in range(2 , number):
        if number % i == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")
            
num_to_check = int(input("Enter number:"))
prime_checker(num_to_check)

            
