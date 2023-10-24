# CTI-110-0004
# P5T1 - Functions
# delrosab1153
# Tue 10/24/2023

def main():
  print("Hello, World!")
  burger = 4.9999
  print_money(burger)
  print_money(4)
  print_money(7)
# main() ends

# Other functions go here
def print_money(amount):
  print("$", format(amount, ".2f"), sep="")


# Now, start the program
main()