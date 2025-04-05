import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    Generate and print N_NUMBERS random integers 
    between MIN_VALUE and MAX_VALUE (inclusive).
    """
    for i in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=' ')
    print()  # Just to move to the next line after printing all numbers

if __name__ == '__main__':
    main()
