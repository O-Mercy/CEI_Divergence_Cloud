#2-2 Pay Check Calculator

hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))

tax_rate = 18

gross_pay = round(hours_worked * hourly_rate, 2)
tax_amount = round(gross_pay * (tax_rate / 100), 2)

take_home_pay = round(gross_pay - tax_amount, 2)

print("Pay Check Calculator")
print(f"Gross Pay: {gross_pay}")
print(f"Tax Rate: {tax_rate}%")
print(f"Tax Amount: {tax_amount}")
print(f"Take Home Pay: {take_home_pay}")