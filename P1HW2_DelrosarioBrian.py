
# A brief description of the project
# Sun 9/3/2023
# CTI-110 P1HW2 - Travel Expense
# Brian M. Delrosario

# 3. Ask user to enter their budget

print("\n" "This program caclulates and displays travel expenses." "\n")
print("Enter whole amounts and omit the $ symbol." "\n")
print("Enter budget:")
budget = int(input())

# 4. Ask user to enter travel destination

print("Enter your travel destination:")
destination = input()
      
# 5. Ask user for amount they will spend on gas

print("How much do you think you'll spend on gas?")
fuel = int(input())

# 6. Ask user for amount they will spend on accommodation

print("Approximately how much will you need for lodging?")
lodging = int(input())

# 7. Ask user for amount they will spend on food

print("Lastly, how much will you need for food?")
food = int(input())

# 8. Add expenses

total_expenses = fuel + lodging + food

# 9. Subtract expenses from budget

balance = budget - total_expenses
print("\n")

# 10. Display results

print("----- ----- Travel Expenses ----- -----" "\n")
print("Destination: ", destination)
print("Initial budget: ", budget, "\n")
print("Fuel: ", fuel)
print("Lodging: ", lodging)
print("Food: ", food, "\n")
print("Remaining balance: ", balance, "\n")
print("You'll have a balance of $", balance, ".")
