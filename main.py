file = "expenses.txt"

def welcome():
    print("Welcome to the Personal Expense Tracker!")
    print("___________________________________")
    print("1. Add expenses")
    print("2. View expenses")
    print("3. Total expenses")
    print("4. Remove expenses")
    print("5. Exit")
    print("------------------------")
    print()


def load_expenses():
    expenses = []

    try:
        with open(file, "r") as f:
            for line in f:
                category, amount = line.strip().split(",")
                expenses.append({"category": category, "amount": float(amount)})
    except FileNotFoundError:
        pass
    except Exception as e:
        print(e)
    return expenses



def save_expenses(expenses): 
    with open(file, "w") as f:
        for e in expenses:
            f.write(f"{e['category']},{e['amount']}\n")


def add_expense(expenses):  
    try:                
        category = input("Enter your category: ")  
        amount = float(input("Enter the amount: "))
        expenses.append({"category": category, "amount": amount})
        save_expenses(expenses)
        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount input. Please enter a valid number.")

    except Exception as e:
        print(e)



def view_expenses(expenses):
    print("\nExpenses:")
    i = 1
    for e in enumerate(expenses, start=1):
        print(f"{i}. Category: {e[1]['category']}, Amount: {e[1]['amount']}")
        i += 1
    print()


def total_expense(expenses):
    total = 0
    for e in expenses:
        total += e['amount']

    print(f"Your Total Expenditure is: {total}")

 
def remove_expense(expenses):
    if not expenses:
        print("No expenses to remove.")
        return
    
    try:
        number = int(input("Enter the number of the expense to remove: "))   
        if 1 <= number <= len(expenses):
            removed_expense = expenses.pop(number - 1)
            save_expenses(expenses)
            print(f"Removed expense: Category: {removed_expense['category']}, Amount: {removed_expense['amount']}")


        else:
            print("Invalid expense number.")
    except ValueError:
        print("Please enter a valid expense number.")
    except Exception as e:
        print(e)


def main():
    welcome()
    expenses = load_expenses()
    while True:
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expense(expenses)

        elif choice == "4":
            remove_expense(expenses)

        elif choice == "5":
            print("Thank you for using the Personal Expense Tracker!")
            return

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()




    