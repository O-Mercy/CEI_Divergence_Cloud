# 4-1 Even or Odd Checker

# #Display title
def main(): 
    print("Even or Odd Checker")
    
    #Get input from user
    user_input = int(input("Enter a number: "))
    output = is_even_or_odd(user_input)
    print(f"The number is: {output}")
    
#Calculate if number is even or odd
def is_even_or_odd(number):
     if number % 2 == 0:
         return "Even"
     else:
         return "Odd"   
   
#Validate user input
# if (user_input = i)
#     print("Valid Input")
#     break 
# else:
#     print("Invalid input. Please enter a valid integer.")

main()