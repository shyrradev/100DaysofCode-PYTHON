#!/usr/bin/env python3
from art import logo
import random
import sys

import os

def clear():
    """Clears the terminal screen."""
    os.system('clear')
play =input("Do you want to play BlackJack game (Yes or No): ")

if play == "yes":
    print(logo)
    print("Let's Play BlackJack Game!")
elif play == "no":
    sys.exit(1)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_card = 0
end_of_game = False
def compare(new_choice):
        if new_choice == 11 and player_card > 21:
            new_choice = 1  
        if new_card == "yes" and player_card + new_choice == 21:
            print("YOU HIT THE BLACK JACK! You win!")
        elif player_card + new_choice > 21:
            print(f"You chose higher than 21, you LOOSE! your card: {player_card + new_choice}  computer's card: {computer_choice}")
        elif player_card + new_choice < computer_choice:
            print(f"YOUR THREE CARDS ARE LOWER THAN COMPUTERS 2 CARDS YOU LOOSE! your card: {player_card + new_choice}  computer's card: {computer_choice}")
        elif player_card + new_choice == computer_choice:
            print(f"YOUR THREE CARDS ARE THE SAME AS COMPUTERS 2 CARDS YOU LOOSE! your card: {player_card + new_choice}  computer's card: {computer_choice}")
        elif player_card + new_choice > computer_choice:
            print(f"YOUR THREE CARDS ARE HIGHER THAN COMPUTERS 2 CARDS YOU WIN! your card: {player_card + new_choice}  computer's card: {computer_choice}")
def compare1():
    if player_card == 21:
        print("You win!")
    elif computer_choice == 21:
        print("You loose computer has BLACKJACK!")
    
while not end_of_game:
    my_first_card = random.choice(cards)
    my_second_card = random.choice(cards)
    my_choice = print(f"Your first cards are: {my_first_card}, {my_second_card}")
    player_card = my_first_card + my_second_card
    computer_choice1 = random.choice(cards)
    computer_choice2 = random.choice(cards)
    print(f"The compouter's first card is: {computer_choice1}")
    computer_choice = computer_choice1 + computer_choice2
    compare1()
    new_choice= random.choice(cards)
    new_card =input("Do you wish to take another card yes or no ")
    #add while loop here

    if new_card == "yes":
        
        print(f"Your third card is {new_choice}")
        print(f"computer's second card is {computer_choice2}")
        compare(new_choice)
    elif new_card == "no": 
        if player_card > computer_choice:
            print(f"You win! you chose higher then computer's cards: your card is {player_card} and the computer's card is {computer_choice}")
        else:
            print(f"You loose! Computer's cards are higher than yours! the computers cards are : {computer_choice}")
    else:
        print("Please type 'yes' or 'no': ")
        break

    game_over = input("Do you want to play again? Type 'y' or 'n': ")
    if game_over == "n":
        end_of_game = True
        print("Thank you for playing!")
        break
        # Exit the loop
    elif game_over == "y":
        clear()
        # Restart the game loop
    else:
            print("Please type 'y' or 'n': ")

    
        
    

