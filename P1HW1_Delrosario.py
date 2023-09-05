"""
CTI 110
P1HW1 - Variables
Delrosario, Brian
Tue 9/5/23

Basic math
1. Request int
2. Square it, cube it
3. Request another int
4. Add them, multiply them

"""
#PART ONE: NUMBERS

# Variables, first, second

first = 0
second = 0

print("NUMBERS" "\n")

print("Enter integer:" "\n")

first = int(input())

print("\n", first, "squared is", first * first)

print("\n" "And", first, "cubed is", first * first * first)

print("\n" "Enter another integer:" "\n")

second = int(input())

print("\n", second, "+", first, "=", second + first)

print("\n", second, "*", first, "=", second * first)

#PART TWO: MOVIES

#Three variables
#int · the year of the movie
#float · the gross (in millions of dollars)
#string · a quote

name = "1917"
year = 2019
gross = 384.6 # millions of dollars
quote = "Down to Gehenna, or up to the Throne, he travels the fastest who travels alone."

print("\n" "\n" "MOVIES" "\n")

#Print out this information
#Then print a movie quote

print("Movie:", name, "\n")

print("Year:", year, "\n")

print("Gross (in millions of USD):", gross, "\n")

print("Quote:", quote, "\n")
