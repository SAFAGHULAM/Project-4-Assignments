import math

def main():
    side1 = float(input("Enter the length of side AB: "))
    side2 = float(input("Enter the length of side AC: "))
    
    side3 = math.sqrt(side1**2 + side2**2)
    print("The length of side BC(hypothenius) is", side3)
    
if __name__ == "__main__":
    main()