print("NUMBER BASES CONVERTER")

print("What do you wish to do?")
print("1. Convert to base 10 \n 2. Convert from base 10 to any base")

operation = int(input("What conversion?:"))

if operation == 1:
   base = int(input("What base?:"))
   number=input("what number do u wish to convert?:")
   if len(number)==1:
      print(f"{number} in base ten= {number}")
   elif len(number)==2:
      last_digit = int(number[1])
      first_digit = int(number[0])

      solution = (first_digit * base ** 1) + (last_digit * base ** 0)
      print(f"{number} in base ten = {solution}")
   elif len(number) == 3:
      last_digit = int(number[2])
      mid_digit = int(number[1])
      first_digit = int(number[0])

      solution = (first_digit * base ** 2) + (mid_digit * base ** 1) +(last_digit * base ** 0)
      print(f"{number} in base ten = {solution}")
   else:
      print("TOO MANY DIGITS, this verion supports only three")


