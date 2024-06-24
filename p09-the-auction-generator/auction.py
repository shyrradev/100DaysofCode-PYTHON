#!/usr/bin/env python3

import my_art
import os
logo = my_art.logo
print(logo)
print("WELCOME TO THE AUCTION GAME")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
dict = {}
max_bid = 0
max_key = 0
condition=  False
while not condition:
    name = (input("Enter your name "))
    bid_amount= int(input("Enter your bid amount: $"))
    user_input = input("Is there anyone else who like to bid? Type yes or no ")
    clear()
    
    if user_input == "no":
        condition = True
    dict[name] = bid_amount
    for name, bid_amount in dict.items():
            if bid_amount > max_bid: 
                max_bid = bid_amount
                max_key = name
print(f"The winner is {max_key.upper()}! and the highest bid is: ${max_bid}!")
        
    
    