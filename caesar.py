
#this is program to encrypt and decrypt caesar Cipher
from secrets import choice


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(v_text,shift_ammount):
    encrypt_text = ""
    for letter in v_text:
        position = alphabet.index(letter)
        new_position = position+shift_ammount
        new_letter = alphabet[new_position]
        encrypt_text += new_letter
    print(encrypt_text)
        

def decrypt(v_text,shift_ammount):
    decrypt_text = ""
    for letter in v_text:
        position = alphabet.index(letter)
        new_position = position-shift_ammount
        new_letter = alphabet[new_position]
        decrypt_text += new_letter
    print(decrypt_text)
        


choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if choice == "encode":
    encrypt(text,shift)
elif choice == "decode":
    decrypt(text,shift)