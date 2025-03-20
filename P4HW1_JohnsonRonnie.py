 # Ronnie Johnson
# 3/20/2025
# P4HW1
# This program collects a user-specified number of scores, validates input, removes the lowest score, calculates the average, and assigns a letter grade.


# Get the number of scores to enter
num_scores = int(input("Enter the number of scores you want to enter: "))
scores = []

# Collect scores with validation
for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score {i+1}: "))
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("Invalid score!!! Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input!!! Please enter a numeric value.")

# Process scores
lowest_score = min(scores)
scores.remove(lowest_score)
average_score = sum(scores) / len(scores)

# Determine letter grade
if average_score >= 90:
    letter_grade = 'A'
elif average_score >= 80:
    letter_grade = 'B'
elif average_score >= 70:
    letter_grade = 'C'
elif average_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display results
print(f"\nLowest score dropped: {lowest_score}")
print(f"Remaining scores: {scores}")
print(f"Average score: {average_score:.2f}")
print(f"Letter grade: {letter_grade}")
