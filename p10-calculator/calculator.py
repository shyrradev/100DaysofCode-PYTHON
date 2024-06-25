#!/usr/bin/env python3

from art import logo

print(logo)
import os

def clear():
    # Clear command for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear command for Unix/Linux/MacOS/BSD
    else:
        os.system('clear')

def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def multi(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1/n2    

dict ={
    "*": multi,
    "+": add,
    "-": sub,
    "/":divide,
}
def calculator():
    while True:
            try:
                num1 = float(input("What's the first number? "))
                break  # Exit the loop if input is a valid integer
            except ValueError:
                print("Please enter a valid integer.")

    for symbol in dict:
        print(symbol)

    condition = True

    while condition == True:
        operation = input("please pick an operation: ")
        while True:
            try:
                num3 = float(input("What's the next number? "))
                break  # Exit the loop if input is a valid integer
            except ValueError:
                print("Please enter a valid integer.")
        operation_symbol = dict[operation]
        answer= operation_symbol(num1,num3)
        answer= round(answer, 2)

        print(f"{num1} {operation} {num3} = {answer}")

        var = input(f"type y to continue calculating with {answer} or type n to exit, new for new calculation: ")
        if var == "y":
            num1 = answer
        elif var == "n":
            condition= False
        elif var == "new":
            clear()
            calculator()
            
calculator()            


