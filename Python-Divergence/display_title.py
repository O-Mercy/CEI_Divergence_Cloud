#3-5 

#Display title
print("Table Of Powers")

#Get two inputs from user(start and stop number)

while True:
    start = int(input ("Start Number: "))
    stop = int(input("Stop number: "))

    # Validate user input
    # Make sure the user enters a start integer that’s less than the stop integer.
    if(start < stop):
        #print("Valid Input")
        break
    else:
        print("Start number should be lower than stop number")
        

#Use a for loop to calculate and print table
print(f"Number  \t Squared  \t Cubed")

for i in range(start, stop+1, 1):
    print(f"{i} \t {i ** 2} \t {i ** 3}")