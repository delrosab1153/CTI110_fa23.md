# CTI-110-0004
# P5HW1 - Math Quiz
# delrosab1153
# Fri 11/3/2023

print("Welcome to Math Quiz")

# Import modules
import random

# The main menu function
def main_menu():
  print("\nMAIN MENU")
  print("____ ____ ____ ____ ____ ____ ")
  print("1. Adding random numbers")
  print("2. Subtracting random numbers")
  print("3. Exit")
  choice = input("\nPlease choose one of the menu options: ")
  if choice == '1':
      addition_question()
  elif choice == '2':
      subtraction_question()
  elif choice == '3':
      print("\nOkay, ending the quiz. 😃")
  else:
      print("\nNot a valid choice. Please, try again.")
      main_menu()


# The addition questions
def addition_question():
  a = random.randint(1, 100)
  b = random.randint(1, 100)
  print(f'\n  {a}')
  print(f'+ {b}')
  
  guesses = 0
  while True:
    answer = int(input('  '))
    guesses += 1

    if answer == (a + b):
      print(f'\nCorrect! {a} + {b} = {a + b}.')
      print(f'\nNumber of guesses: {guesses}')
      main_menu()
    elif answer < (a + b):
      print('\nSorry, guess is too low. Try again.\n')
    else:
      print('\nSorry, guess is too high. Try again.\n')


# The subtraction questions
def subtraction_question():
  a = random.randint(1, 100)
  b = random.randint(1, 100)
  print(f'\n  {a}')
  print(f'- {b}')
  
  guesses = 0
  while True:
    answer = int(input('  '))
    guesses += 1

    if answer == (a - b):
      print(f'\nCorrect! {a} - {b} = {a - b}.')
      print(f'\nNumber of guesses: {guesses}')
      main_menu()
    elif answer < (a - b):
      print('\nSorry, guess is too low. Try again.\n')
    else:
      print('\nSorry, guess is too high. Try again.\n')


# Main function
def main():
  print("\nP5HW1 - Math Quiz (Addition and Subtraction)")
  main_menu()
  print("\nThank you for playing... Bye!!")

main()