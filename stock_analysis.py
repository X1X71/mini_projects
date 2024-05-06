# Prices for $AMC over a 20 day period
stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]  

def price_at(i):   
    return stock_prices[i-1]  

def max_price(a, b):   
    return max(stock_prices[a-1: b])  

def min_price(a, b):   
    return min(stock_prices[a-1: b])   

while True:
    user_choice = input("\nMake a selection 1-4:\n1. Price of given day: (1-20)\n2. Max price in range: (1-20)\n3. Min price in range: (1-20)\n4. Exit\n")

    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice == 1:
            i = int(input("Which day would you like to see the price of $AMC? (1-20)\n "))
            print ("Price at day", i, "is", price_at(i))
        elif user_choice == 2:
            a = int(input("Enter first day in range: (1-20)\n "))
            b = int(input("Enter second day in range: (1-20)\n "))
            print ("Max price between day", a, "and", b, "is", max_price(a, b))
        elif user_choice == 3:
            a = int(input("Enter first day in range: (1-20)\n "))
            b = int(input("Enter second day in range: (1-20)\n "))
            print ("Min price between day", a, "and", b, "is", min_price(a, b))
        elif user_choice == 4:
            print("You have decided to exit. Goodbye!\n")
            break
        else:
            print("Invalid choice, please try again.\n")
    else:
        print("Invalid input. Please enter a digit.\n")
