def get_total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += float(expense['amount'])
    return total

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)

def add_expense(expenses,description,amount):
    expenses.append({'description': description, 'amount': amount})
    print(f"Added expense: {description.title()}, Amount: {amount}")

def show_budget_detail(budget, expenses):
    print(f"Your total budget is: {budget}")
    print("Your expenses are:")
    for expense in expenses:
        print(f"- {expense['description'].title()}: {expense['amount']}")
    print(f"Total Spent: {get_total_expenses(expenses)}")
    print(f"Remaining Budget: {get_balance(budget, expenses)}")

def main():
    print("Welcome to the Budget App!")
    initial_budget = float(input("Enter your budget: "))
    # filepath = 'budget_data.json'  # Define the path to your JSON file
    # initial_budget, expenses = load_budget_data(filepath)

    budget = initial_budget
    expenses = []

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            description = input("Enter a expense description: ")
            amount = float(input("Enter a expense amount: "))
            add_expense(expenses,description,amount)
        elif choice == '2':
            show_budget_detail(budget, expenses)
        elif choice == '3':
            print("Exiting the Budget App.")
            break
        else:
            print('Invalid input, please enter 1, 2 or 3.')



if __name__ == "__main__":
    main()