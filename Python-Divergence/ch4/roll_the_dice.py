import random
#4-2
def main():
    #TODO While loop to continue the program
    while True:
        choice = input("Roll the dice? (y/n: ")
        if choice.lower () != "y":
            print("Goodbye1")
            break       #TODO Exit statement
    
        #TODO Dispaly Title
        print("Dice Roller")
        die1 = rolldice()
        die2 = rolldice()
        print(f"Die 1: {die1}")
        print(f"Die 2: {die2}")
        
        total = die1 + die2
        print(f"Total: {total}")
        
        if total == 2:
            print("Snake eyes!")
        elif total == 12:
            print("Boxcars!")   #TODO Check the return and display special messages


#TODO Function to roll dice, return value between 1-6
def rolldice():
    val = random.randint(1,6)
    return val

main()

