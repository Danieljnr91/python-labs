word = input("Enter the word:")

lists = list(word)

reverse = lists[::-1]


if lists == reverse:
    print(f"{word} is a palindromic word")
else:
    print(f"{word} is not a palindromic word")    


