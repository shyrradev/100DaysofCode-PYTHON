#!/usr/bin/env python3




#Treasure Hunt Game

print("Welcome to the Treasure Hunt Game")
print("You are in the treasure MAZE and have to find the TREASURE ARE YOU READY?")

ans= input("You are at the cross road, choose where to go. Type left or right ")

if ans == "right":
        print("You fell into a hole. Game Over")
elif ans == "left":
        ans= input("You come to a lake. Type wait to wait for a boat. Type swim to swim across ")
        if ans == "swim":
            print("You swam across and got attacked by an angry trout. Game Over")
        elif ans == "wait":
            ans= input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose ")
            if ans == "red":
                print("It's a room full of fire. Game Over")
            elif ans == "yellow":
                print("You found the treasure! You Win!")
            elif ans == "blue":
                print("You enter a room of beasts. Game Over")
            else:
                print("You chose a door that doesn't exist. Game Over")
else:
        print("wrong input, choose left or right")
