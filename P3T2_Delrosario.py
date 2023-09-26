"""
CTI 110
P3T2 - Choices and Menus
delrosab1153
Tue 9/26/2023
"""

# Simple program, with main()

def main():
  #Print the menu
  print ("\n", "-"*10, "Main Menu", "-"*10, "\n")
  print("1. Exchange virtual high-fives", "\n")  
  print("2. Ponder the utility of school", "\n")
  print("3. Receive free tokens", "\n")

  # User chooses
  print("Your choice? ", end="")
  choice = int(input())
  print("\n" "You chose:", choice)

  #Branch (if) on choice
  if choice == 1:
    option_1()
  elif choice == 2:
    option_2()
  elif choice == 3:
    option_3()
  else:
    print("Sorry, that's not an option.")

def option_1():
  print ("\n" "🙌 Exchange virtual high-five, yes or no")
  high_five = input()
  if high_five == "yes":
    print("\n" "Smickity smack!  Back at you!")
  elif high_five == "Yes":
    print("\n" "Aw, snap!  Back at you!")
  elif high_five == "Y":
    print("\n" "Whaaat?!  Back at you!")
  elif high_five == "y":
    print("\n" "Smickity smack!  Back at you!")
  else:
    print("\n" "No worries.")

def option_2():
  print ("\n" "🤔 Do you find traditional formal school useful?  Yes, no?")
  school_utility = input()
  if school_utility == "yes":
    print("\n" "🤓 Okay.  I'm feelin' that.")
  elif school_utility == "Yes":
    print("\n" "🤓 Okay.  I'm feelin' that.")
  elif school_utility == "Y":
    print("\n" "🤓 Okay.  I'm feelin' that.")
  elif school_utility == "y":
    print("\n" "🤓 Okay.  I'm feelin' that.")
  else:
    print("\n" "🙂 For sure, school could use fixing.")

def option_3():
  print ("\n" "😉 I got about 10 free tokens.  How many do you want?")
  free_tokens = int(input())
  if 1<= free_tokens <=10:
    print("\n" "Here you go.")
  else:
    print("\n" "🙂 Gotcha.  No time for distraction.  I like your diligence.")

# Start the program

main()

