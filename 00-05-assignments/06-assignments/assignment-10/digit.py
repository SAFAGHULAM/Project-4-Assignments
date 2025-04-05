def print_ones_digit(num: int):
    """Prints the ones digit of the given number."""
    ones_digit = num % 10  # Get the ones digit using the modulo operator
    print(f"The ones digit is {ones_digit}")

def main():
    # Prompting the user to input a number
    num = int(input("Enter a number: "))
    
    # Calling the function to print the ones digit
    print_ones_digit(num)

# This ensures the main function is executed when the script runs
if __name__ == '__main__':
    main()
