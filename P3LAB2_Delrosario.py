# P3LACB2 - Letter Grade Converstion
# Tue 9/26/2023
# CTI-110-004
# Brian M. Delrosario

# This program takes a number grade (0-100) and converts it into a letter grade.

# Receive number grade.

print("\n" 'Enter a number grade, 0 through 100.')

num_grade = float(input("\n" "What's the number grade? "))

# Display results.

if 100 < num_grade:
    print("\n" 'Your grade is:  A (greater than 100)')
elif 90 <= num_grade <= 100:
    print("\n" 'Your grade is:  A')
elif 80 <= num_grade < 90:
    print("\n" 'Your grade is:  B')
elif 70 <= num_grade < 80:
    print("\n" 'Your grade is:  C')
elif 60 <= num_grade < 70:
    print("\n" 'Your grade is:  D')
elif 0 <= num_grade < 60:
    print("\n" 'Your grade is:  F')
else:
    print("\n" 'Check input; not within grading range.')
