letters = ['A','b','C','D','E','F','G','H','i','_','k','l','n','M','N','O','P','Q','R','S','T','U','v','w','x','y','z']

v = input("Enter letter:")
length = len(letters)

for i in range(length):
    if letters[i] == '_':
        letters[i] = v
print(letters)