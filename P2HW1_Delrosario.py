# Travel expense calculator
# Fri 9/8/2023
# CTI-110 P2HW1 - Travel
# Brian M. Delrosario

# 4. Ask user to enter travel destination

print("\n" "This program caclulates and displays travel expenses." "\n")

print("Enter your travel destination:")
destination = str(input())

# 3. Ask user to enter their budget

print("\n" "Enter dollars amounts ONLY (omit the $ symbol)." "\n")

print("Enter budget:")
budget = int(input())

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
print("Destination:              ", destination)
print("Initial budget:           ", "$" f'{budget:.2f}', "\n")
print("Fuel:                     ", "$" f'{fuel:.2f}')
print("Lodging:                  ", "$" f'{lodging:.2f}')
print("Food:                     ", "$" f'{food:.2f}', "\n")
print("----- ----- ----- ----- ------ ----- --" "\n")
print("Remaining balance:        ", "$" f'{balance:.2f}', "\n")
