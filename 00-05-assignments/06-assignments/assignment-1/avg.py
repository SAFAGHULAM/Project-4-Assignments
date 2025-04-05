# Write a function that takes two numbers and finds the average between the two

def main():
    # Get two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate the average
    average = (num1 + num2) / 2

    # Print the result
    print(f"The average of {num1} and {num2} is {average}")
    
if __name__ == "__main__":
    main()