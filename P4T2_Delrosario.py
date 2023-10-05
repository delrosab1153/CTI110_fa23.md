# CTI-110-0004
# P4T2 - Timecard
# delrosab1153
# Thu 10/5/2023

# Get the user's work info for the week
# Find the pay

"""
hours = [8, 9, 10, 7, 9]
print("You worked: ")
total_hours = sum(hours)
print(total_hours, "hours")
print("Longest shift was", max(hours), "hours")
print("Shortest shift was", min(hours), "hours")
# Find the average
average = total_hours / len(hours)
print("For an average of", average, "hours per shift.")
"""

# Description: Take 2, by hand

print("Timecard program")

# Variables: 

DAYS_OF_WEEK = 5 # Constant
todays_hours = 0
total_hours = 0

# Input: Ask for time worked for each day

for day in range(DAYS_OF_WEEK):
    print("Hours worked for day", day+1, end=": ") # We'll print 1-5, not 0-4
    todays_hours = float(input())

    #total_hours = total_hours + todays_hours
    total_hours += todays_hours # Shortcut += operator

# Output: Print the total and average hours

print("\n""Total hours this week:", total_hours)
print("Average hours this week:", total_hours / DAYS_OF_WEEK, "\n")

