#JohnsonRonnie
#2/24/25
#P2HK2
#Use list to capture student grades

#Get 6 grades from the user-they should be floats
grade1 = float(input('Enter grade for module1:'))
grade2 = float(input('Enter grade for module2:'))
grade3 = float(input('Enter grade for module3:'))
grade4 = float(input('Enter grade for module4:'))
grade5 = float(input('Enter grade for module5:'))
grade6 = float(input('Enter grade for module6:'))

#create an empty list
grades= []

#Use the append method to add all grades into the list
#Code looks like this: list_name.append(what_to_add_to_list

grades.append(grade1)
grades.append(grade2)
grades.append(grade3)
grades.append(grade4)
grades.append(grade5)
grades.append(grade6)

#Display the list
print(grades)
print()

#Display values to user
print("---------Results-------------")
print(f"{'Lowest Grade:':<20}{min(grades)}")
print(f"{'Highest Grade:':<20}{max(grades)}")
print(f"{'Sum of Grade:':<20}{sum(grades)}")
average=sum(grades)/len(grades)
print(f"{'Average:':<20}{average:.2f}")
print("-.*"*25)