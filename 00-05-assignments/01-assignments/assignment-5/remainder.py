# this program will take two numbers and return the remainder of the division of the two numbers

def main():
    # get the first number
    num1:int = int(input("Enter the first number to be divided: "))
    # get the second number
    num2:int = int(input("Enter the second number to divide by: "))
    # calculate the quotient
    quotient:int = num1 // num2
    # calculate the remainder
    remainder:int = num1 % num2
    
    print("The result of the division is ", quotient, " with a remainder of ", remainder)
    
if __name__ == "__main__":
    main()