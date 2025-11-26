print("SUMS NUMBERS BETWEEN ENTERED RANGE")

print("Enter range of number seperated by comma")

ranges = input("Enter Range:").split(",")

int_range =[]
for i in ranges:
    int_range.append(int(i.strip()))

first = int_range[0]
second = int_range[1]

total = 0

for j in range(first , second + 1):
    total += j
print(total)



