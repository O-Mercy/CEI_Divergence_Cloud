
#Display title
def display_title():
    print("Tip Calculator")    
    
#Calculate cost function 

def cost_of_meal():
    while True:
        try:
            meal_cost = float(input("Cost of meal: "))
        except ValueError:
            print("Must be valid decimal number. Please try again.")


#calculate tip percent function

def get_tip_percent():
    while True:
        try:
            tip_percent = int(input("Tip percent: "))
        except ValueError:
            print("Must be valid integer. Please try again.")  
            continue
        if tip_percent <= 0:
            print("Must be greater than 0. Please try again.")
        else:
            return tip_percent
        
        
              
#Function for Tip amount and total 
tip_percent = float(input("Tip percent: "))

tip_amount = round(cost_of_meal * (tip_percent / 100), 2)

total_amount = round(cost_of_meal + tip_amount, 2)


#Main function
def main():
    display_title()
    print("INPUT")
    
    meal_cost = cost_of_meal
    tip_percent = get_tip_percent
    print()
    
    print("Cost of meal: ")
    print("Tip percent: ")
    
    print(f"Tip amount: {tip_amount}")
    print(f"Total amount: {total_amount}")
    
    print("OUTPUT")
    print("Cost of meal: meal:", meal_cost)
    print("Tip percent:", (tip_percent) + "%")
    print("Tip amount:" , tip_amount)
    print("Total amount:", total_amount)
    
    
    
    main()   
    