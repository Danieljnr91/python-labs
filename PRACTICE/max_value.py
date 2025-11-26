# print("Enter list of numbers seperated by spaces")

# numbers = input("Enter numbers:").split(" ")

# int_numbers = []
# for i in numbers:
#     int_numbers.append(int(i.strip()))

# first_digit = int_numbers[0]
# last_digit = int_numbers[-1]

# max_num = first_digit

# for j in int_numbers:
#     if j > max_num:
#        max_num= j

# print(max_num)



numbers = input("Numbers:").split()

int_num = [int(i) for i in numbers]

first = int_num[0]

for j in int_num:
    if j > first:
        first = j
print(first)
    

