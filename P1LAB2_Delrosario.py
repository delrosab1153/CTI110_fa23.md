"""
CTI110
P1LAB2 - Sales
delrosab1153
8/31/2023

Simple point-of-sale (POS) program.

"""

# Set up our store

store_name = "Shoes R Us"
product = "shoes"
stock = 20
price = 49.99

# Greet customer

print("😀 Welcome to", store_name, "\n")
print("What's your name?" "\n")
customer_name = input()
print("\n" "Nice to meet you,", customer_name,"!")

# Explain product

print("\n" "👞 Our special today is:", product)
print("\n" "On sale for: $", price)
print("\n" "Only", stock, "left! 🥳")

# Receive order

print("\n" "How many pairs of", product, "would you like?" "\n")
# Input gives us a string
#order = input()
# Convert it to a number
#order = int(order)
order = int(input())

# Finish up

total_price = order * price
print("\n" "👍 So you'd like" "\n")
print(order, product, "for a total of $", total_price)

# Optional

if (order > stock):
  order = stock
  print("\n" "🙂 Sorry, we can only sell you", order)

total_price = order * price
print("\n" "That's", order, product)
print("\n" "for a total of $", total_price)
print("\n" "<y/n>" "\n", sep="")
confirm = input()
if(confirm == "y"):
  print("\n" "Shipped!")
else:
  print("\n" "Order canceled.")

print("\n" "Thanks for shopping with us!")
