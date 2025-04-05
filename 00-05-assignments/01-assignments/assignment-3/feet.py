# this programme will convert feet to inches.

inches_foot: int = 12 # 1 foot = 12 inches

def main():
    feet: float = float(input("Enter the number of feet: "))
    inches: float = feet * inches_foot
    print("That is", inches, "inches!")
    
if __name__ == "__main__":
    main()