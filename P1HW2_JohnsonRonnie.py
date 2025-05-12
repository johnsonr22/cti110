# Your Name
# Date
# Assignment Name
# This program calculates the remaining budget after travel expenses.

# Get user inputs
budget = float(input("	$4,785: "))
destination = input("Tokyo: ")
gas_expense = float(input("$3.50: "))
accommodation_expense = float(input("$200+ per night: "))
food_expense = float(input("$50 - $75 per day: "))

# Calculate total expenses
total_expenses = gas_expense + accommodation_expense + food_expense
remaining_budget = budget - total_expenses

# Display results
print(f"\nTravel Destination: {destination}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")

if remaining_budget < 0:
    print("Warning: You have exceeded your budget!")
else:
    print("You are within your budget.")
