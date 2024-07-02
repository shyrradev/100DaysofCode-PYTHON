#!/usr/bin/env python3

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 800,
    "milk": 200,
    "coffee": 100,
}

def check_resources(prompt):
    for key, amount in MENU[prompt]["ingredients"].items():
        if resources.get(key, 0) < amount:
            print(f"Sorry, there is not enough {key}.")
            return False
    return True
def making_order(prompt):
    items = MENU[prompt]['ingredients']
    for item, amount in items.items():
        resources[item] -= amount
    print(f"Here is your {prompt} ☕️. Enjoy!")

def add_resources():
    for key in resources.keys():
        resources[key] += int(input(f"How much {key} do you want to add? "))

def check_money(prompt, money, profit):
    if money >= MENU[prompt]['cost']:
        making_order(prompt)
        profit += MENU[prompt]['cost']
        change = money - MENU[prompt]['cost']
        print(f"Your change is ${change:.2f}.")
        return profit
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return profit

profit = 0
machine_should_continue = True

while machine_should_continue:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: ${profit}")
    elif prompt == "off":
        machine_should_continue = False
    elif prompt == "add resources":
        add_resources()
    elif prompt in MENU:
        if check_resources(prompt):
            money = float(input("Please insert money in $: "))
            profit = check_money(prompt, money, profit)
