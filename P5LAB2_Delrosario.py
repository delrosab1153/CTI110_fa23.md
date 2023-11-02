# CTI-110-0004
# P5LAB2 - Functions
# delrosab1153
# Thu 11/2/2024


# Print a table of squares
def main():
  print("P5T2 - Squares")
  print("\nNumber\t\tNumber Squared")
  for num in range(1,11):
    num_squared = square(num)
    print_row(num, num_squared)


# Square the inputted number
def square(num):
  square = num * num
  return square


# print_row() is a void function
def print_row(num, num_squared):
    print(num, "\t\t\t", num_squared)


# Start program
main()
