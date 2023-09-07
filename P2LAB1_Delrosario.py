"""
CTI 110
P2LAB1 - Gas Prices
Delrosario
Thu 9/7/2023

Driving is expensive. Write a program with a car's gas milage (miles/gallon) and the cost of gas (dollars/gallon) as floating-point input, and output the gas cost for 20 miles, 75 miles, and 500 miles.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:

print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')

Ex: If the input is:

  20.0, 3.1599

where the gas mileage is 20.0 mi/gal and the cost of gas is $3.1599/gal, the output is:

  3.16, 11.85, 79.00

Note: Real per-mile cost would also include maintenance and depreciation.


"""

# Ask for MPG

miles_per_gallon = float(input("What's the car's miles per gallon (MPG)? "))

# Ask for price per gallon of gasoline

price_per_gallon = float(input("\n" "Price per gallon? $ "))

# Show the price per mile to drive, or $/miles

price_per_mile = price_per_gallon / miles_per_gallon

# print("This vehicle costs $", price_per_mile, "to drive one mile.")

print("\n" "This vehicle costs $", f'{price_per_mile:.2f}', "to drive one mile.")

# Given 20.0 miles

print("\n" "To drive 20 mi, this vehicle costs $" f'{(20*price_per_mile):.2f}' ".")

# Given 20.0 miles and $3.1599 per gal

print("\n" "To drive 20 mi at $3.1599 per gal, this vehicle costs $" f'{(20*(3.1599 / miles_per_gallon)):.2f}' ".")

print("\n" "Given 75 miles and $", f'{price_per_gallon:.2f}', "per gal, this vehicle costs $" f'{(75*price_per_mile):.2f}' ".")

print("\n" "Given 500 miles and $", f'{price_per_gallon:.2f}', "per gal, this vehicle costs $" f'{(500*price_per_mile):.2f}' ".")
