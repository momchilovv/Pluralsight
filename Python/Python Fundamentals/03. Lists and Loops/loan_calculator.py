# Get the loan information
money_owned = float(input("How much money do you owe? "))
apr = float(input("What's the annual percentage rate of the loan? "))
payment = float(input("How much will you pay off each month? "))
months = int(input("How many months do you want to see the results for? "))

# Calculate the monthly rate
monthly_rate = apr / 100 / 12

for i in range(months):
    # Calculate the interest
    interest_paid = money_owned * monthly_rate
    # Add the interest to the money you still owe
    money_owned = money_owned + interest_paid

    # Check if the loan is paid off
    if(money_owned - payment < 0):
        print(f"Last payment is: ${money_owned}")
        print(f"You paid the loan in {i + 1} months")
        break
    
    # Make the payment
    money_owned -= payment

    # Print the results
    print(f"Paid ${payment:.2f} of which ${interest_paid:.2f} was interest.")
    print(f"Still owe: ${money_owned:.2f}")
