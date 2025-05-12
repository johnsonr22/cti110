#Ronnie Johnson
#3/3/2025
#P3LAB
#Use if/else statements to determine coin combination

#Get a float from user and convert your integer 
money=float(input("Enter the amount of money as a float: $"))

money=int(money *100)

print(money)

#Calculate number of whole dollars
num_dollars = money//100
print(f"Num dollars:{num_dollars}")

#Remove the dollars from the amount of money
money=money -(num_dollars * 100)

print(f"The remaining money is:{money}")


#Calculate number of whole quarters
num_quarters = money//25
print(f"Num quarters:{num_quarters}")

#Remove the quarters from the amount of money
money=money -(num_quarters * 25)

print(f"The remaining money is:{money}")

#Calculate number of whole dimes
num_dimes = money// 10
print(f"Num dimes:{num_dimes}")

#Remove the dimes from the amount of money
money=money -(num_dimes * 10)

print(f"The remaining money is:{money}")


#Calculate number of whole nickels
num_nickels = money//5
print(f"Num nickels:{num_nickels}")

#Remove the nickels from the amount of money
money=money -(num_nickels * 5)

print(f"The remaining money is:{money}")
num_pennies =money//1