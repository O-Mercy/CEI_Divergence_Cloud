#2-1 Student Registration
first_name = (input("Enter first name:\t"))
last_name = (input("Enter last name:\t\t"))
birth_year = float(input("Enter birth year:\t"))

full_name = f"{first_name}{last_name}"
temp_password = f"{first_name}*{birth_year}"


print("Student Registration")
print(f"\nWelcome {full_name}!")
print("Your registration is complete")
print(f"Your temporary password is: {temp_password}")