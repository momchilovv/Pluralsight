expenses = []

number_of_expenses = int(input("Enter the number of expenses you want to record: "))

for i in range(number_of_expenses):
    expenses.append(float(input("Enter an expense: ")))

print(f"You spent ${sum(expenses):.2f}")