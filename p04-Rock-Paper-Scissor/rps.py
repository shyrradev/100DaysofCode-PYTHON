#!/usr/bin/env python3

import random
rock= '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


list= [rock, paper, scissors]
num_list= len(list)
comp_choice= random.randint(0, num_list -1)


user_input= input("What do you choose? 0 for rock, 1 for paper, and 2 for scissor \n")
user_input = int(user_input)



if user_input == 0:
    print("You chose rock!")
    print(rock)
    
    if comp_choice == 0:
            print (rock)
            print("I chose the same. It's a tie")
    elif comp_choice == 1:
            print(paper)
            print("I chose paper! I WIN")
    elif comp_choice == 2:
            print(scissors)
            print("I chose scissors, you win!")


if user_input == 1:
    print("You chose paper!")
    print(paper)
    if comp_choice == 0:
            print(rock)
            print("I chose rock, you win!")
    elif comp_choice == 1:
            print(paper)
            print("I chose paper, it's a tie")
    elif comp_choice == 2:
            print(scissors)
            print("I chose scissors, I win!")
if user_input == 2:
    print("You chose scissors!")
    print(scissors)
    if comp_choice == 0:
        print (rock)
        print("I chose rock, I win!")
    elif comp_choice == 1:
        print(paper)
        print ("I chose paper, you win!")
    elif comp_choice == 2:
        print(scissors)
        print("I chose scissors, it's a tie")

