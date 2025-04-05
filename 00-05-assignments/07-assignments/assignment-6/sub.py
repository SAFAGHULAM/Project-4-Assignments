def subtract_seven(num):
    """
    Subtracts 7 from the given number and returns the result.
    """
    return num - 7

def main():
    number = int(input("Enter a number: "))
    result = subtract_seven(number)
    print(f"{number} minus 7 is {result}")

# Call the main function to run the program
if __name__ == '__main__':
    main()
