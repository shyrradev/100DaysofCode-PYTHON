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
    print("User chose rock!")
    print(rock)
    print(f"Computer chose {comp_choice}")
    if comp_choice == 0:
            print (rock)
            print("It's a tie")
    elif comp_choice == 1:
            print(paper)
            print("Computer wins")
    elif comp_choice == 2:
            print(scissors)
            print("User wins")


if user_input == 1:
    print("User chose paper!")
    print(paper)
    print(f"Computer chose {comp_choice}")
    if comp_choice == 0:
            print(rock)
            print("User wins")
    elif comp_choice == 1:
            print(paper)
            print("It's a tie")
    elif comp_choice == 2:
            print(scissors)
            print("Computer wins")
if user_input == 2:
    print("User chose scissors!")
    print(scissors)
    print(f"computer chose {comp_choice}")
    if comp_choice == 0:
        print (rock)
        print("Computer wins")
    elif comp_choice == 1:
        print(paper)
        print ("User wins")
    elif comp_choice == 2:
        print(scissors)
        print("It's a tie")

