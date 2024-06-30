#!/usr/bin/env python3
from art import logo
from art import vs
from game_data import data
import random
import os

def clear():
    os.system('clear')
    
print(logo)

print("WELCOME TO WHOSE GOT MORE FOLLOWERS GAME!")
final_score=0

while True:
    typea= random.choice(data)
    typeb=random.choice(data)
    if typea == typeb:
        typeb=random.choice(data)
    print(f"Compare A: {typea['name']}, a {typea['description']}, from {typea['country']}")
    print(vs)
    print(f"Compare B: {typeb['name']}, a {typeb['description']}, from {typeb['country']}")
    choice=input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == "a" and typea['follower_count'] > typeb['follower_count']:
        print("Yay, you're correct!")
        final_score += 1
    elif choice == "b" and typeb['follower_count'] > typea['follower_count']:
        print("Yay, you're correct!")
        final_score += 1
    
    else:
        print("Nay")
        print(f"SORRY YOU LOST! Your final score is {final_score}")
        break
    clear()
    print(f"Your final score is {final_score}")
           
        
        


