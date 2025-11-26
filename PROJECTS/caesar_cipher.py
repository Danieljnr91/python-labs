import time 

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'

]

def encryption(plain_text , shift_key):
  cipher_text = ""
  for char in plain_text:
    char_pos = alphabet.index(char)
    new_char_pos = char_pos + shift_key % 26
    new_char = alphabet[new_char_pos]
    cipher_text = cipher_text + new_char
  print(f"{plain_text} has been encrypted to {cipher_text}")



def decryption(cipher_text , shift_key):
  plain_text = ""
  for char in cipher_text:
    char_pos = alphabet.index(char)
    new_char_pos = char_pos - shift_key % 26
    new_char = alphabet[new_char_pos]
    plain_text = plain_text +new_char
  print(f"{cipher_text} has been decrypted to {plain_text}")


end_action = False
while not end_action:
  word = input("Enter word to be encyrpted:")
  shift = int(input("Enter shift key:"))
  print("1.Encrypt \n 2.Decrypt")
  action = int(input("What do you wish to do?:"))
  if action == 1:
    print("Encrypting...")
    time.sleep(2)
    encryption(plain_text = word , shift_key = shift)
  else:
    print("Decrypting...")
    time.sleep(2)
    decryption(cipher_text = word , shift_key = shift)

  redo = input("Do you wish to perfome again?(Y/N):").lower()
  if redo == 'y':
    continue
  else:
    end_action = True
    print("Alright, Exiting...")




    