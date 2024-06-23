#!/usr/bin/env python3

import art_py
import sys

logo = art_py.logo
print(logo)

alphabet = 'abcdefghijklmnopqrstuvwxyz'

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
        else:
            cipher_text += letter  # Preserve non-alphabet characters
    return cipher_text  # Return the encrypted or decrypted text

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction in ["encode", "decode"]:
        break  # Exit the loop if input is valid
    else:
        print("Please input valid choice: 'encode' or 'decode'")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypted_message = cipher(text, shift, direction)
print(f"The {direction}d text is: {encrypted_message}")
