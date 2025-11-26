ranges = input("Enter range:").split(",")

int_range = [int(i.strip()) for i in ranges]

first = int_range[0]
second = int_range[1]

for j in range(first , second):
    if j % 5 == 0 and j % 3 == 0:
        print("FuzzBuzz")
    elif j % 3 == 0:
        print('Fuzz')
    elif j % 5 == 0:
        print("Buzz")
    else:
        print(j)