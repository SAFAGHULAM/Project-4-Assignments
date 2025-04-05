import random

def guess_the_number():
    # Computer selects a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Guess the Number game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while not guessed:
        # Ask for the player's guess
        try:
            player_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        # Check if the guess is correct
        if player_guess < number_to_guess:
            print("Too low! Try again.")
        elif player_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            guessed = True

# Start the game
guess_the_number()
