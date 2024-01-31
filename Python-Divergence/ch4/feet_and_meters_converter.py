#4-3 Feet and Meters Converter
def display_title():
    print("Feet and Meters Conversion")

# TODO Display menu function
def menu():
    print("Conversions Menu")
    print("a. Feet to Meters")
    print("b. Meters to Feet")

# TODO Feet to meter

def feet_to_meter(feet):
    meters = feet * 0.3048
    return meters
    

# TODO meter to feet function

def meter_to_feet(meters):
    feet = meters / 0.3048
    return feet

def main():
    display_title()
    menu()
    
    choice = input("Select a conversion (a/b): ")
    
    if choice.lower() == 'a':
        feet = float(input("Enter Feet: "))
        # result = feet_to_meter(feet)
        # print(result)
        print(feet_to_meter(feet))
    elif choice.lower() == 'b':
        meter = float(input("Enter Meter: "))
        print(meter_to_feet(feet))

main()


