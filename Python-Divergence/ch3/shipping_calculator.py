#3-4 Shipping calculator

print("Shipping Calculator")

choice = "y"
while (choice = "y")
items_cost = float(input("Enter Cost of Items: "))
if items_cost < 30 :
    shipping_cost = 5.95
elif items_cost >= 30 and items_cost <= 49.99:
    shipping_cost = 7.95
elif items_cost >=50 and items_cost <= 74.99:
    shipping_cost = 9.95
elif items_cost >= 75:
    shipping_cost = 0

print("Shipping Cost: ", shipping_cost)
print("Total Cost: ", shipping_cost + items_cost)
