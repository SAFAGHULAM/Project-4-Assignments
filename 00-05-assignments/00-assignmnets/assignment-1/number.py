# this program will help to get two inputs from the user and will perform the addition operation on them.

def main():
    # get first input from the user
    num1: str = input("Enter first number: ")
    # conversion of string to integer
    num1: int = int(num1)
    # get second input from the user
    num2: str = input("Enter second number: ")
    # conversion of string to integer
    num2: int = int(num2)
    # addition of two numbers
    total: int = num1 + num2
    print ("The total is " + str(total) + ".") 
    
if __name__ == "__main__":
    main()