 # Ronnie Johnson

 # 3/10/2025

 # P3HW2

 # Determine employee's regular pay, OT pay, and gross pay

# Pseudocode

# Get the employee details
employee_name = input("Enter the employee's name: ")
hours_worked = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the employee's pay rate: "))

# Calculate pay and overtime

if hours_worked > 40:
    # Calculate overtime
    OT_hours = hours_worked - 40
    OT_pay_rate = pay_rate * 1.5
    OT_pay = OT_hours * OT_pay_rate
    
    # Regular pay (for 40 hours)
    reg_hours = 40
    reg_pay = reg_hours * pay_rate
    
    # Gross pay (regular + overtime)
    gross_pay = OT_pay + reg_pay

else:
    # No overtime
    OT_hours = 0
    reg_hours = hours_worked  # Regular hours are equal to hours worked
    
    reg_pay = reg_hours * pay_rate
    gross_pay = reg_pay  # No overtime pay

# Display results
print(f"{'Hours Worked':<20}{'Pay Rate':<20}")
print("------" * 20)
print(f"{hours_worked:<20}{pay_rate:<20}")
print(f"Overtime Hours: {OT_hours}")
print(f"Regular Pay: ${reg_pay}")
print(f"Overtime Pay: ${OT_pay if OT_hours > 0 else 0}")
print(f"Gross Pay: ${gross_pay}")
