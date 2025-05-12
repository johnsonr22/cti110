# Ronnie Johnson
# 3/27/2025
# P4HW2
# This program calculates gross pay for multiple employees, including overtime pay. 
# Pseudocode:

# Create outer loop that runs until user input "Done"

# Create the accumulator variables
total_regular_pay = 0
total_overtime_pay = 0
total_gross_pay = 0
employee_count = 0

# Main loop for entering employee data
employee_name = input("Enter employee name or 'Done' to terminate: ")
while employee_name.lower() != "done":
    print(f"Calculating pay for {employee_name}")
    
    # Get pay rate and hours worked from user
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    hours_worked = float(input(f"How many hours did {employee_name} work? "))

    # Check for overtime (hours > 40) and calculate pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)  # Overtime is 1.5x regular pay
        regular_pay = 40 * pay_rate
    else:
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate

    # Calculate gross pay
    gross_pay = regular_pay + overtime_pay

    # Add to the accumulator variables
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Print results for the current employee
    print(f"Regular pay: ${regular_pay:.2f}")
    print(f"Overtime pay: ${overtime_pay:.2f}")
    print(f"Gross pay: ${gross_pay:.2f}")
    
    # Ask if the user wants to enter another employee or terminate
    employee_name = input("Enter another employee's name or 'Done' to terminate: ")

# Program has terminated, display final totals
print("\nFinal Totals:")
print(f"Total regular pay for all employees: ${total_regular_pay:.2f}")
print(f"Total overtime pay for all employees: ${total_overtime_pay:.2f}")
print(f"Total gross pay for all employees: ${total_gross_pay:.2f}")
print(f"Number of employees entered: {employee_count}")
print("End of program......")