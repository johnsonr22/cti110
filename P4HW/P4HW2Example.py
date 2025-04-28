#Create outer loop that runs until user input"Done"

#Create the accumulator variables
total_subtotal = 0
total_tax = 0
grand_total = 0

item_name =input ("Enter item name or 'Done' to terminate:")
while item_name.lower() !="done":
    print(f"Loop is running bc you put in {item_name}")
#In hw, below is your print statements    
    quanity=int(input(f"How many {item_name} will you buy?"))
    price=float(input (f"How much does {item_name} cost?"))

    #Code to Caculate the values
    total_item_cost = quanity * price
    tax= total_item_cost * .06
    tax= total_with_tax = total_item_cost + tax

    #Add to the accumulator variabes
    total_subtotal += total_item_cost
    total_tax += tax
    grand_total += total_with_tax

    #In hw, below is your print statements
    print(f"Subtotal: ${total_item_cost:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total with tax: ${total_with_tax:.2f}")
    print("Loop is running")
    
    item_name=input("Enter item name or 'Done' to terminate")
#Loop has broken, display final accumulated totals below
print()
print()
print(f"the total for all tems BEFORE tax is ${total_subtotal:.2f}")
print(f"The total tax on all items is ${total_tax:.2f}")
print(f"The total for all items including tax is ${grand_total:.2f}")
print("End of program......")