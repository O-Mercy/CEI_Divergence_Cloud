#3-2 Tip Calculator

print("Cost of meal: ")

meal_cost = float(input())
tip_percentage = 0.15
print("15%")

tip_amt = meal_cost * tip_percentage
total_amt = meal_cost + tip_amt
tip_amt = round(tip_amt, 2)
total_amt = round(total_amt, 2)
print(f"Tip amount:   ${tip_amt}")
print(f"Total amount: ${total_amt}")

tip_percentage = 0.20
print("20%")

tip_amt = meal_cost * tip_percentage
total_amt = meal_cost + tip_amt
tip_amt = round(tip_amt, 2)
total_amt = round(total_amt, 2)
print(f"Tip amount:   ${tip_amt}")
print(f"Total amount: ${total_amt}")

tip_percentage = 0.25
print("25%")

tip_amt = meal_cost * tip_percentage
total_amt = meal_cost + tip_amt
tip_amt = round(tip_amt, 2)
total_amt = round(total_amt, 2)
print(f"Tip amount:   ${tip_amt}")
print(f"Total amount: ${total_amt}")