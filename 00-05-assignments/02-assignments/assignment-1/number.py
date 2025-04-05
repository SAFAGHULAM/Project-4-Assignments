# this programme will take a list of numbers and return the sum of the numbers in the list

def add_all_numbers(numbers) -> int:
    total_far: int = 0
    for number in numbers:
        total_far += number
        
    return total_far

def main():
    numbers = [1, 2, 3, 4, 5]
    print(add_all_numbers(numbers))
    
if __name__ == "__main__":
    main()