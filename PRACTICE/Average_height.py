print("AVERAGE HEIGHT CHECKER")

print("Enter heights seperated by commas")
heights = input("Enter Heights:").split(",")



int_height = []
for i in heights:
    int_height.append(int(i.strip()))

height1 = int_height[0]
height2 = int_height[-1]

total_height = 0
length = len(heights)

for j in int_height:
    total_height += j
average = total_height / length
print(f"Average height = {average}")





