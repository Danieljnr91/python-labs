import random
import time

symbol_list = ["+", "-", "*", "/", "=", "<", ">", "≤", "≥", "√"]

word = input("What word do u wish to encode:")
length = len(word)

comp_symbols = random.choices(symbol_list , k = length)

print("encrypting...")
time.sleep(3)
encrypted = "".join(comp_symbols)
print(f"Your word has bn encrypted to {encrypted}")

decrypt = input("Do you wish to decrypt?(Y/N):").lower()
if decrypt == "y":
    print("decrypting...")
    time.sleep(3)
    print(f"Decrypted into {word} ")
else:
    print("Alright")