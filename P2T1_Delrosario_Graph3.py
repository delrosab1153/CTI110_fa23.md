"""
CTI-110
Delrosario
Tue 9/12/2023
"""



"""
print("😜 Enter Pokemæn data")

print("Day 1: ", end="")
day1 = int(input())

print("Day 2: ", end="")
day2 = int(input())

print("Day 3: ", end="")
day3 = int(input())

# Put the data in a list

data = [day1, day2, day3]


# To-do: Graph the real data

fig, ax = plt.subplots()
ax.plot([1, 2, 3], data)
plt.title("Pokemæn Data 😜")
plt.xlabel('Day #')
plt.ylabel('Pokemæns Collected')
plt.show()
"""



# New version · Loop, get each day at a time

import matplotlib.pyplot as plt

# Collect the data

data = [] # Empty list

num_days = int(input("How many days? "))

for day in range(num_days):
  print("Day ", day, ":", end="")
  today = int(input())
  data.append(today) # Add to end of list

# Put the data in a list (DONE)

# Print min and max

print("Best day: ", max(data))
print("Worst day: ", min(data))

# To-do: Graph the real data

fig, ax = plt.subplots()
ax.plot(range(num_days), data)
plt.title("Pokemæn Data 😜")
plt.xlabel('Day #')
plt.ylabel('Pokemæn Collected')
plt.show()