# CTI-110-0004
# P4T3 - Three loops
# delrosab1153
# Tue 10/10/2023
"""
Write three loops

 1. For loop
 2. While loop
 3. While with sentinel

Ask the user how many cars s/he saw today

Find the total and the average
"""
cars_today = 0
cars_total = 0
day = 1
MAX_DAYS = 5

# 1 - for loop

print("Enter how many cars you saw each day over", MAX_DAYS, "days")
for day in range(1, MAX_DAYS + 1):
  print("Day", day, end=": ")
  cars_today = int(input())
  cars_total += cars_today
print("Total # of cars seen: ", cars_total)
average = cars_total / MAX_DAYS
print("Average per day: ", average)
print()

# 2 - while loop

cars_today = 0
cars_total = 0
day = 1

print("Enter how many cars you saw each day over", MAX_DAYS, "days")
while day <= MAX_DAYS:
  print("Day #", day, end=": ")
  cars_today = int(input())
  cars_total += cars_today
  day += 1
print("Total # of cars seen: ", cars_total)
average = cars_total / MAX_DAYS
print("Average per day: ", average)
print()

# 3 - sentinel

cars_today = 0
cars_total = 0
day = 0

print("Enter how many cars you saw each day.")
print("Enter -1 to finish.")
DONE_VALUE = -1
# If user types this, finish
# Go until user says to stop with DONE_VALUE

keep_going = True
while keep_going:
  print("Cars seen today:", end="")
  cars_today = int(input())
  if cars_today == DONE_VALUE:
    # Exit
    keep_going = False
  else:
    # Add value to total
    cars_total += cars_today
    day += 1
print("Total cars: ", cars_total)
print("Over", day, "days")
average = cars_total / day
print("Average per day: ", average)
