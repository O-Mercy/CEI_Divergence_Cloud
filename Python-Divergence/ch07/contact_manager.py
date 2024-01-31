#6-3

#Display menu
def main():
    contacts = [["Eric Idle, eric@ericidle.com, +44 20 7946 0958"],
                    ["Mike Murach, mike@murach.com, 559-123-4567"]]
    
    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the Contact Management Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-5).\n")


#Display function menu

def display_menu():
    print("Contact Manager")
    print("1. List")
    print("2. View ")
    print("3. Add")
    print("4. Delete")
    print("5. Exit")
    print()


#Functions for menu options
def list_contacts(contacts):
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact[0]} - {contact[1]}")
    print()
    
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.\n")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact[0]} - {contact[1]}")
        print()
        
def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    contacts.append([name, phone])
    print("Contact added successfully.\n")      
    
def edit_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        contact_number = int(input("Enter the number of the contact to edit: ")) - 1
        if 0 <= contact_number < len(contacts):
            new_name = input("Enter the new name: ")
            new_phone = input("Enter the new phone number: ")
            contacts[contact_number] = [new_name, new_phone]
            print("Contact edited successfully.\n")
        else:
            print("Invalid contact number. Please enter a valid contact number.\n")
    except ValueError:
        print("Invalid input. Please enter a valid contact number.\n")

def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        contact_number = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= contact_number < len(contacts):
            deleted_contact = contacts.pop(contact_number)
            print(f"Contact {deleted_contact[0]} deleted successfully.\n")
        else:
            print("Invalid contact number. Please enter a valid contact number.\n")
    except ValueError:
        print("Invalid input. Please enter a valid contact number.\n")
          


if __name__ == "__main__":
    main()
    