# CTI-110-0004
# P4HW1 - Score List
# Fri 10/13/2023
# Brian M. Delrosario

# Variables, number of scores, list of scores

num_scores = int(input("How many scores do you want to enter? "))
list_scores = [] #Empty list, to hold scores


# Loop thru number of scores, get input from user
# This was the hard part

print("Enter a score between 0 and 100.")

for i in range(1, num_scores + 1, 1):

  # From P4T3, while loop
  valid_score = False
  while not valid_score:

    score = float(input(f"Enter score #{i}: "))

    if 0 <= score <= 100:
      list_scores.append(score) # Append, textbook chap. 8.2.3
      valid_score = True

    else:
      print("INVALID SCORE; RE-ENTER SCORE.")


# Print valid scores

avg = sum(list_scores) / len(list_scores)

print("\n" "----------- Results --------------")

print("Lowest score    :", min(list_scores))
print("Modified list   :", list_scores)
print("Scores average  :", avg)

# Determine letter grade for average, from P3HW1

if avg >= 90:
    print("Grade:          : A")
elif avg >= 80:
    print("Grade:          : B")
elif avg >= 70:
    print("Grade:          : C")
elif avg >= 60:
    print("Grade:          : D")
else:
    print("Grade:          : F")

print("----------------------------------")
