# P3HW1 - Homework Content
# Sat 9/23/2023
# CTI-110-004
# Brian M. Delrosario

# This program takes a number grade, determines average, and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter number grade for Module 1 of 6: '))
mod_2 = float(input('Enter number grade for Module 2 of 6: '))
mod_3 = float(input('Enter number grade for Module 3 of 6: '))
mod_4 = float(input('Enter number grade for Module 4 of 6: '))
mod_5 = float(input('Enter number grade for Module 5 of 6: '))
mod_6 = float(input('Enter number grade for Module 6 of 6: '))

# Add grades entered to a list

grades = [mod_1,mod_2,mod_3,mod_4,mod_5,mod_6]

# Determine lowest, highest, sum, and average for grades

low = min(grades)
high = max(grades)
sum_of_grades = sum(grades)
avg = sum_of_grades/6

# Display results

print("\n" "----------- Results --------------")

print("Lowest grade:        ", min(mod_1, mod_2, mod_3, mod_4, mod_5, mod_6))
print("Highest grade:       ", max(mod_1, mod_2, mod_3, mod_4, mod_5, mod_6))
print("Sum of grades:       ", sum_of_grades)
print("Average:             ", f'{avg:.2f}')

print("----------------------------------")

# Determine letter grade for average

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')
