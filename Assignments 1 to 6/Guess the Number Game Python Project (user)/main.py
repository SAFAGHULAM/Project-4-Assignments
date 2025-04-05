print("Welcome to 'Guess the Number'!")
print("Think of a number between 1 and 100, and I will try to guess it.")

low = 1
high = 100
attempts = 0

# The computer tries to guess the number
while True:
    attempts += 1
    guess = (low + high) // 2  # The computer guesses the middle number
    
    # Ask the user if the guess is correct, too high, or too low
    feedback = input(f"Is your number {guess}? (Enter 'h' for too high, 'l' for too low, 'c' for correct): ").lower()

    if feedback == 'c':
        print(f"Yay! I guessed your number {guess} in {attempts} attempts.")
        break
    elif feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1
    else:
        print("Invalid input. Please enter 'h', 'l', or 'c'.")
