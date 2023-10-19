# CTI 110
# P4LAB2
# Time Card
# delrosab1153
# Thu 10/19/2023

# This program will act like a time card reader,
# adding up each day's hours to get the total.

# Version 1 - uses numbers for days
# Change line below if it's a 7 day week
DAYS_IN_WEEK = 5
totalHours = 0 # The total starts at zero

print("Please enter your hours worked.\n")

for day in range(DAYS_IN_WEEK):
    print("Hours for day", day+1, ": ", end="")
    hoursToday = float(input())
  
    # Input validation is a loop inside this loop
    while (hoursToday < 0 or hoursToday > 24):
      print("Must enter 0 through 24. Try again.")
      # Ask again
      print("Hours for day", day+1, ": ", end="")
      hoursToday = float(input())
    totalHours = totalHours + hoursToday # Add to running total

# Print the total
print("You worked a total of", totalHours, "hours this week.")

# Print the average
avgHours = totalHours / DAYS_IN_WEEK
print("For an average of", format(avgHours, "0.2f"), "hours per day.")

# Show how printing money works
perHour = float(input("Enter wage (dollars per hour): $"))
grossPay = perHour * totalHours
print(f'If you made ${perHour:.2f} per hour.')
print(f'Your gross pay would be ${grossPay:.2f}.')