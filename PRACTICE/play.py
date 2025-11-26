numbers = input("Enter numbers sep by comma:").split(",")

int_num = [int(i.strip()) for i in numbers]

even =[]
odd = []

for j in int_num:
    if j % 2==0:
        even.append(j)
    else:
        odd.append(j)

print(f"even numbers = {even}")
print(f"odd numbers = {odd}")

