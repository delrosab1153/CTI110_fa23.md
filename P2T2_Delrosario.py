"""
CTI-110
Delrosario
Thu 9/14/2023
"""

# New version · Loop, get each day at a time

import matplotlib.pyplot as plt
import turtle

# Collect the data

data = [] # Empty list

  # num_days = int(input("How many days? "))

num_days = turtle.numinput("Input", "How many days?")
num_days = int(num_days)

# Put the data in a list (DONE)

for day in range(num_days):
  # print("Day ", day, ":", end=" ")
  # today = int(input())
  label = "Day #" + str(day) # Day 1 and on
  today = turtle.numinput("Next day", "How many Pokemæn?")
  data.append(today) # Add to end of list

# Print min and max

print("Best day: ", max(data))
print("Worst day: ", min(data))

# To-do: Total and average

total = 0
for num in data:
  total += num
  # total is now all the numbers in data, summed

average = total / num_days
print("Total:", total)
print("Average:", average)

# To-do: Graph the real data

fig, ax = plt.subplots()
ax.plot(range(num_days), data)
plt.title("Pokemæn Data 😜")
plt.xlabel('Day #')
plt.ylabel('Pokemæn Collected')
plt.show()
