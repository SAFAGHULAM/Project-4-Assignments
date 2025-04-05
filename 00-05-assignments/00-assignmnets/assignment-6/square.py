# this program will take a number and return the square of that number

def main():
    # get the number from the user
    number: int = int(input("Type a number to get the square of it: "))
    num = float(number)
    # calculate the square of the number
    square = num * num
    # print the result
    print(num, "squared is", square)
    
if __name__ == "__main__":
    main()