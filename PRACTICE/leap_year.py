#algorithm for leap year
#divisible by 4 = possible leap year
#divisible by 100 = not a leap year
#divisible by 400 = leap year

year = int(input("What year?:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print( print(f"{year} is not a leap year"))
    else:
        print(f"{year} is a leap year")

else:
    print(f"{year} is not a leap year")

