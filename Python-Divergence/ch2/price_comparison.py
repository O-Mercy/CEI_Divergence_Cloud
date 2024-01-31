#2-4 Price Comparison

price_64 = float(input("Price of 64 oz size: "))
price_32 = float(input("Price of 32 oz size: "))

oz_64 = 0.09
oz_32 = 0.11

price_per_64oz = round (price_64 / oz_64, 2)
price_per_32oz = round (price_32 / oz_32, 2)

print("Price Comparison")
print(f"Price per ounce for 64 ounces: {price_per_64oz}")
print(f"Price per ounce for 32 ounces: {price_per_32oz}")