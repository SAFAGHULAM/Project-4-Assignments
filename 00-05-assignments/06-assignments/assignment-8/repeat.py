def print_multiple(message: str, repeats: int):
    """Prints the message 'repeats' number of times."""
    for _ in range(repeats):
        print(message)

def main():
    # Prompting the user for the message and number of repeats
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    
    # Call the function to print the message multiple times
    print_multiple(message, repeats)

# This part ensures the main function is executed when the script runs
if __name__ == '__main__':
    main()
