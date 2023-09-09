# Student grade calculator
# Fri 9/8/2023
# CTI-110 P2HW2 - Grades
# Brian M. Delrosario

# Pseudocode
"""

Define variable modX and input scores

  modX = float input 'Enter grade for Module X'

Define variable sum and average

Display results

  Print min
  Print max
  Print sum
  Print average
  
"""

# Ask user for the student's scores (out of 100) for Modules 1 through 6

print("This program caclulates a student's grades (out of 100 pts.) for Mod. 1 thru 6." "\n")

mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

# Define variable sum and average

sum = mod1 + mod2 + mod3 + mod4 + mod5 + mod6
average = sum / 6

# Display results

print("\n" "----------- Results --------------")

print("Lowest grade:        ", min(mod1, mod2, mod3, mod4, mod5, mod6))
print("Highest grade:       ", max(mod1, mod2, mod3, mod4, mod5, mod6))
print("Sum of grades:       ", sum)
print("Average:             ", f'{average:.2f}')

print("----------------------------------")
