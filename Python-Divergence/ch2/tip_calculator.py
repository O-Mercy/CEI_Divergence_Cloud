#2-3 Tip Calculator

cost_of_meal = float(input("Cost of meal: "))
tip_percent = float(input("Tip percent: "))

tip_amount = round(cost_of_meal * (tip_percent / 100), 2)

total_amount = round(cost_of_meal + tip_amount, 2)

print("Tip Calculator")
print(f"Tip amount: {tip_amount}")
print(f"Total amount: {total_amount}")