#7-2

FILENAME = "wizard_all_items.txt"
INVENTORY_FILENAME = "wizard_inventory.txt"

def read_items():
    items = []
    with open(FILENAME) as file:
        for line in line:
            line = line.replace("\n", "")

def read_inventory():
    inventory = []
    with open(INVENTORY_FILENAME) as file:
        for line in line:
            line = line.replace("\n", "")
            inventory. append(line)
    return inventory        
    
    
def display_title():
    print("The Wizard Inventory Program")
    print()
    
def display_menu():    
    print("COMMAND MENU")
    print("1. walk - walk down on the beach")
    print("2. show - Show all items")
    print("3. Drop an Item")
    print("4. Exit")
    print()


def walk(inventory):
    items = read_items()
    
def show_inventory(inventory):
    if not inventory:
        print("The inventory is empty.")
    else:
        print("Inventory:")
        for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item}")
    print()

def grab_item(inventory):
    if len(inventory) >= 4:
        print("You can't carry more than four items. Drop something first.\n")
    else:
        item = input("Enter the item to grab: ")
        inventory.append(item)
        print(f"{item} has been grabbed.\n")

def edit_item(inventory):
    show_inventory(inventory)
    if not inventory:
        return

    try:
        item_number = int(input("Enter the number of the item to edit: ")) - 1
        if 0 <= item_number < len(inventory):
            new_item = input(f"Enter the new name for {inventory[item_number]}: ")
            inventory[item_number] = new_item
            print(f"{new_item} has been edited.\n")
        else:
            print("Invalid item number. Please enter a valid item number.\n")
    except ValueError:
        print("Invalid input. Please enter a valid item number.\n")

def drop_item(inventory):
    show_inventory(inventory)
    if not inventory:
        return

    try:
        item_number = int(input("Enter the number of the item to drop: ")) - 1
        if 0 <= item_number < len(inventory):
            dropped_item = inventory.pop(item_number)
            print(f"{dropped_item} has been dropped.\n")
        else:
            print("Invalid item number. Please enter a valid item number.\n")
    except ValueError:
        print("Invalid input. Please enter a valid item number.\n")

def main():
    wizard_inventory = ["Wooden Staff", "Wizard Hat", "Cloth Shoes"]

    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_inventory(wizard_inventory)
        elif choice == '2':
            grab_item(wizard_inventory)
        elif choice == '3':
            edit_item(wizard_inventory)
        elif choice == '4':
            drop_item(wizard_inventory)
        elif choice == '5':
            print("Exiting the Wizard Inventory Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-5).\n")

if __name__ == "__main__":
    main()
    