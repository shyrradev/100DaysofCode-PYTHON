#!/usr/bin/env python3



import sys

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def cipher(plain_text, shift_amount, direction):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = (position + shift_amount) % 26  # Wrap around using modulus
            elif direction == "decode":
                new_position = (position - shift_amount) % 26  # Wrap around using modulus
            new_letter = alphabet[new_position]
            cipher_text += new_letter
     

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
if direction not in ["encode", "decode"]:
    print("Please input valid choice: 'encode' or 'decode'")
    sys.exit(1)
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypted_message = cipher(text, shift, direction)
print(f"The {direction}d text is: {encrypted_message}")