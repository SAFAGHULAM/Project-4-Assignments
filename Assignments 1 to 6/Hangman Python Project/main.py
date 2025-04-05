import random

def hangman():
    # List of words to choose from
    words = ["python", "hangman", "programming", "developer", "computer"]
    word_to_guess = random.choice(words)
    guessed_word = ["_"] * len(word_to_guess)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Guess the word. You have 6 attempts.")
    
    while attempts > 0:
        print("\nCurrent word: " + " ".join(guessed_word))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Remaining attempts: {attempts}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue
        
        guessed_letters.append(guess)

        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Oops! '{guess}' is not in the word.")

        if "_" not in guessed_word:
            print("\nCongratulations! You've guessed the word:", word_to_guess)
            break

    if attempts == 0:
        print(f"\nSorry, you've run out of attempts! The word was: {word_to_guess}")

# Start the game
hangman()
