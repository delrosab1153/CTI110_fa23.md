# CTI-110-0001
# P3LAB1 - Leap Year
# delrosab1153
# Thu 9/21/23

# Calculate if a year is a leap year

"""
Leap Year

1) The year must be divisible by 4

2) If the year is a century year (1700, 1800, etc.), the year must be evenly divisible by 400; therefore, both 1700 and 1800 are not leap years

Write a program that takes in a year and determines whether that year is a leap year.
"""

is_leap_year = False

print("What year are we checking? ")

year = int(input())

# If year is divisibly by 4, then leap year
# Use %, the modulo operator

if year % 4 == 0:
  is_leap_year = True

# Century exception; if divisible by 100, then NOT a leap year
# Unless it's ALSO divisible by 400, making it a leap year

if year % 100 == 0:
  is_leap_year = False # Then NOT a leap year unless ALSO div by 400
  if year % 400 == 0:
    is_leap_year = True # Then IS a leap year

# Output the answer

if is_leap_year:
  print(year,"is a leap year.")
else:
  print(year,"is not a leap year.")

