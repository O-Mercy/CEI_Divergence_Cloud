def get_quarterly_sales():
    quarterly_sales = []

    for quarter in range(1, 5):
        while True:
            try:
                sales = float(input(f"Enter sales for Q{quarter}: "))
                quarterly_sales.append(round(sales, 2))
                break
            except ValueError:
                print("Invalid input. Please enter a valid sales amount.")

    return quarterly_sales

def calculate_statistics(quarterly_sales):
    total_sales = round(sum(quarterly_sales), 2)
    average_sales = round(total_sales / len(quarterly_sales), 2)
    lowest_sales = round(min(quarterly_sales), 2)
    highest_sales = round(max(quarterly_sales), 2)

    return total_sales, average_sales, lowest_sales, highest_sales

def main():
    #Display Title
    print("The Quarterly Sales program")
    
    quarterly_sales = get_quarterly_sales()

    total_sales, average_sales, lowest_sales, highest_sales = calculate_statistics(quarterly_sales)


    print("\nResults:")
    print(f"Total Sales: ${total_sales}")
    print(f"Average Quarter Sales: ${average_sales}")
    print(f"Lowest Quarter Sales: ${lowest_sales}")
    print(f"Highest Quarter Sales: ${highest_sales}")

if __name__ == "__main__":
    main()


