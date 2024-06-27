#!/usr/bin/env python3
import random
from art import art
import sys


print(art)
print("Welcome to the number guessing game! ")
print("I am thinking of a number between 1 and 100. Can you guess what it is?")

comp= random.choice(range(0,101)) # random number between 1 and 100

attempts = 0

diff=input("Choose a difficulty: 'easy' or 'hard': ") 
if diff == "easy":
    attempts = 10
    print(f"you have {attempts} attempts to play this game!")
elif diff == "hard":
    attempts = 5
    print(f"you have {attempts} attempts to play this game!")

else: 
    print("please choose one. 'easy' or 'hard'")

while attempts > 0:  # loop until attempts = 0
    guess =int(input("Choose a number: "))
    attempts -= 1
    if comp == guess:
        print(f"you guessed it right! You win! the number was {guess}")
    elif comp > guess:
        print("too low. Choose again")
        print(f"you have {attempts} attempts left")
    elif comp < guess:
        print ("too high. Choose again")
        print(f"you have {attempts} attempts left")
    else:
        print("Choose correct value")
        break
if attempts == 0: # if attempts = 0
    print("You ran out of attempts you LOOSE!")
        
        