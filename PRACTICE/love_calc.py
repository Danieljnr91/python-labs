print("LOVE CALCULATOR")

first_name = input("Whats your name:").lower()
second_name = input("Whats your partner's name:").lower()

combined = first_name + second_name

t = combined.count('t')
r = combined.count('r')
u = combined.count('u')
e = combined.count('e')

l = combined.count('l')
o = combined.count('o')
v = combined.count('v')


true_score = t + r + u + e 
love_score = l + o + v 

percentage_score = int(str(true_score) + str(love_score))

print(f"You guys are {percentage_score}% compatible!")



   