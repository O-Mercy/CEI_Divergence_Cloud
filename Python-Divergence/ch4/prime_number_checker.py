    #Display Title
def title():
    print("Prime Number")    

    #Prime number
def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        # Check divisibility up to the square root of the number
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True
    
    
    #Factors
def get_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors    


    #Main function
def main():
    title()
        
        
    while True:
        num_to_check = int(input("Enter a number between 1 and 5000: "))

        if 1 <= num_to_check <= 5000:
            if is_prime(num_to_check):
                print(f"{num_to_check} is a prime number.")
            else:
                print(f"{num_to_check} is NOT a prime number. Factors: {get_factors(num_to_check)}")
        else:
            print("Please enter a number between 1 and 5000.")

        try_again = input("Do you want to try again? (y/n): ")
        if try_again.lower() != 'y':
            print("Bye!")
            break

if __name__ == "__main__":
    main()






