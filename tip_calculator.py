print("Welcome to the tip calculator.")
# handle input and convert for calculation
bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# handle adding the bill with the chosen tip percentage and then round
bill_with_tip = bill + ((bill * tip_percent) / 100)
pay_amount = round(bill_with_tip / people, 2)
print(f"Each person should pay: ${pay_amount:.2f}")