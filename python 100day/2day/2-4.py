print("Welcome to the tip calculator")
total_bill = float(input("what was the total bill? $"))
tip_percentage = int(input("what percentage tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))

cal = total_bill * (1 + tip_percentage / 100) / people
new_cal = round(cal, 2)
new_cal = "{:.2f}".format(new_cal)
print(f"Each person should pay:${new_cal}")
