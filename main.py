# Rock Paper Scissors Game by Anushka Chinoy

import random


# function to print game starting menu
def display_menu():
    menu = ("\n--- Rock Paper Scissors Game ---\n"
            + "Rules: \n"
            + "Rock vs Paper --> Paper wins \n"
            + "Paper vs Scissors --> Scissors wins \n"
            + "Rock vs Scissors --> Rock wins \n")
    print(menu)


# function to validate input against options
def input_validation(choice, options):
    while choice not in options:
        print("Please enter a valid option.")
        choice = input("Enter your choice: ").lower()
    return choice


# function to carry out random computer selection
def computer_selection():
    options = {1: "rock", 2: "paper", 3: "scissors"}
    random_choice = random.randint(1, 3)
    computer_choice = options[random_choice]
    return computer_choice


# function to evaluate and print the winner
def evaluate_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        winner = "DRAW :O \n"
    elif ((user_choice == "paper" and computer_choice == "rock")
          or (user_choice == "scissors" and computer_choice == "paper")
          or (user_choice == "rock" and computer_choice == "scissors")):
        winner = "USER WINS! :) \n"
    else:
        winner = "COMPUTER WINS :( \n"
    print(winner)


# function to handle continuing or quitting game
def play_again(response):
    if response == "y":
        print("\n\n")
        main()
    else:
        print("Thanks for playing ;) \n")
        quit()


# main game function
def main():
    # print game menu
    display_menu()

    # get user's choice
    game_choice = input("Enter your choice of 'Rock', 'Paper', or 'Scissors' OR 'q' to quit: ").lower()
    game_options = ["rock", "paper", "scissors", "q"]
    user_choice = input_validation(game_choice, game_options)
    if user_choice == "q":
        play_again("n")
    print("User choice: ", user_choice)

    # get computer's choice
    computer_choice = computer_selection()
    print("Computer choice: ", computer_choice)

    # determine and show the winner
    evaluate_winner(user_choice, computer_choice)

    # get user input to start new game or not
    play_choice = input("Would you like to play again? (Y/N): ").lower()
    play_options = ["y", "n"]
    response = input_validation(play_choice, play_options)
    play_again(response)


# call to main function to start the game
main()
