# Day2 - The Tip Calculator

print("Welcome, to the Tip Calculator !")

total_bill = float(input("What was the total bill? $\n"))

tip_perc = input("What percentage of tip would you like to give? 10, 12, or 15%\n")

tip= float(int(tip_perc)/100)+1

guests = int(input("How many people to split\n"))

to_pay = round((total_bill/guests)*tip, 2)

print(f"Each Person should pay ${to_pay}")