# CTI-110-0004
# P5LAB1 - CYOA
# delrosab1153
# Thu 10/26/2023
# Feel free to fork this REPL and make changes.

# first function: main_menu().

def main_menu():
    print("Main Menu")
    print("\n  You're in front of a spooky old house...")
    print("\nDo you:")
    print("1. Try the front door")
    print("2. Sneak around back 🤫")
    print("3. 🙄 Forget it and go home")
    print("4. Leave a business card, and then go home 😎\n")
    choice = input("Choose: ")
    if choice == '1':
        choice_front_door()
    elif choice == '2':
        choice_back_door()
    elif choice == '3':
        choice_go_home()
    elif choice == '4':
        print("Ok, quitting game 😃")
        return
    else:
        print("That's not a valid choice, please try again.")
        main_menu()


# now we have the choice functions. Feel free to add more.
def choice_front_door():
    print("\n  You try the front door. It's locked.")
    print("\nDo you:")
    print("1. Check around back")
    print("2. Give up and go home 🥱\n")
    choice = input("Choose: ")
    if choice == '1':
        choice_back_door()
    elif choice == '2':
        choice_go_home()
    else:
        print("You have to choose...")
        choice_front_door()


def choice_back_door():
    print("\n  Nope. Also locked.")
    print("\n1. Walk back to the front door. Why? Just 'cause. 😐")
    print("2. Screw it. 😬 Kick in the door.")
    print("3. Be sneaky. Check the windows. 🤫")
    print("4. Give up and go home.\n")
    choice = input("Choose: ")
    if choice == '1':
        choice_front_door()
    elif choice == '2':
        print("\n  Werewolves jump out at you!\n\n  ...You negotiate for repairs.😕 In exchange for them agreeing not to sue, you agree to pay for the repairs and go home.  Whew!\n")
    elif choice == '3':
        sneak_in_through_window()
    else:
        choice_go_home()


def sneak_in_through_window():
    print("\n  🤔 Hmmm. A window is unlocked. And, slightly ajar.")
    print("\n1. Walk back to the front door. 😐")
    print("2. Let's do this. We're going in.")
    print("3. Eh. Let's just go home.\n")
    choice = input("Choose: ")
    if choice == '1':
        choice_front_door()
    elif choice == '2':
        enter_through_unlocked_window()
    elif choice == '3':
        choice_go_home()
    else:
        choice_go_home()

# One way to get into the house 
def enter_through_unlocked_window():
    print("\n  To be continued... 🕵️‍♂️")
    


def choice_go_home():
   print("\n  🤠 Moving on to new adventures.")


# finally, we have main -- which we use to start the program 
def main():
    print("M5LAB1 - Choose Your Own Adventure")
    main_menu()
    print("\nThanks for playing!")

#start the program
main()
