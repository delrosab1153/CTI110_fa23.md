import matplotlib.pyplot as plt

# Collect the data

data = [] # Empty list
print("Enter Pokemæn data")

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
plt.title("Pokemæn Data")
plt.xlabel('Day #')
plt.ylabel('Pokemæns Collected')
plt.show()
