#rock papper scissor:
import random

# Print multiline instruction
print('The Rules are:\n'
      + "Rock VS Paper -> Paper wins \n"
      + "Rock VS Scissors -> Rock wins \n"
      + "Paper VS Scissors -> Scissors wins \n")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # Take the input from user
    choice_user = int(input("Enter your choice: "))

    # Looping until user enters valid input
    while choice_user > 3 or choice_user < 1:
        choice_user = int(input('Invalid Choice'))

    # Initialize value of choice_name variable corresponding to the choice value
    if choice_user == 1:
        choice_name = 'Rock'
    elif choice_user == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    # Print user choice
    print('User choice is:', choice_name)
    print("Now it's Computer's Turn...")

    # Computer chooses randomly any number among 1, 2, and 3
    computers_choice = random.randint(1, 3)

    # Initialize value of comp_choice_name variable corresponding to the choice value
    if computers_choice == 1:
        computers_choice_name = 'Rock'
    elif computers_choice == 2:
        computers_choice_name = 'Paper'
    else:
        computers_choice_name = 'Scissors'

    print("Computer choice is:", computers_choice_name)
    print(choice_name, 'vs', computers_choice_name)

    # Determine the winner
    if choice_user == computers_choice:
        result = "DRAW"
    elif (choice_user == 1 and computers_choice == 2) or (computers_choice == 1 and choice_user == 2):
        result = 'Paper'
    elif (choice_user == 1 and computers_choice == 3) or (computers_choice == 1 and choice_user == 3):
        result = 'Rock'
    elif (choice_user == 2 and computers_choice == 3) or (computers_choice == 2 and choice_user == 3):
        result = 'Scissors'

    # Print the result
    if result == "DRAW":
        print("<--- It's a Draw! --->")
    elif result == choice_name:
        print("<--- Human wins! --->")
    else:
        print("<--- Computer wins! --->")

    # Ask if the user wants to play again
    print("Do you want to play again? (Y/N)")
    answer = input().lower()
    if answer == 'n':
        break

# After coming out of the while loop, print thanks for playing
print("Thanks for playing!")
