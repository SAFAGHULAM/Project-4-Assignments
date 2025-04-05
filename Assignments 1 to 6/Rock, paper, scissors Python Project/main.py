import random

def rock_paper_scissors():
    # Define the choices
    choices = ["rock", "paper", "scissors"]

    print("Welcome to Rock, Paper, Scissors!")

    # Player's choice
    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Validate player's input
    if player_choice not in choices:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        return

    # Computer's choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

# Start the game
rock_paper_scissors()
