#!/usr/bin/env python3


print("Welcome to the Tip Calculator")

total_bill=float((input("what was the total bill? ")))
tip=float((input("how much would you like to tip? 10, 12, or 15% ")))
bill_split=float(input("how many people are splitting the bill? "))

tip_amount=(total_bill * tip / 100)

total_bill_tip= total_bill + tip_amount
split_amount=total_bill_tip / bill_split

final_tip_amount=round(tip_amount, 2)
final_split_amount=round(split_amount, 2)

print(f"The tip is {final_tip_amount} and the bill split amount is {final_split_amount}")

