def count_even(lst):
    # Populating the list with user inputs
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break  # Stop the loop if the user presses enter without entering a number
        try:
            num = int(user_input)  # Try to convert the input to an integer
            lst.append(num)  # Add the number to the list
        except ValueError:
            print("Please enter a valid integer.")  # Handle invalid input

    # Count and print the number of even numbers in the list
    even_count = sum(1 for num in lst if num % 2 == 0)
    print(f"Number of even numbers: {even_count}")

# Example usage
numbers = []
count_even(numbers)
