# this programme will give perimeter of triangle

def main():
    # get the sides of the triangle
    side1: float = float(input("What is the length of the first side of the triangle? "))
    side2: float = float(input("What is the length of the second side of the triangle? "))
    side3: float = float(input("What is the length of the third side of the triangle? "))
    
    # print the perimeter
    print("The perimeter of the triangle is", str(side1 + side2 + side3))
    
if __name__ == "__main__":
    main()