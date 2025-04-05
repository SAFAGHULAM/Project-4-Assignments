# List Practice

fruit_lst = ['apple', 'banana', 'orange', 'grape', 'pineapple']

# Print the length of the list.
lst_length = len(fruit_lst)
print(lst_length)

# Add 'mango' at the end of the list. 
fruit_lst.append('mango')

# Print the updated list.
for fruit in fruit_lst:
    print(fruit)
    
# Index Game

def access_element(lst, index):
    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    return "Index out of range."


def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        old_value = lst[index]
        lst[index] = new_value
        return f"Replaced '{old_value}' with '{new_value}'"
    return "Index out of range."


def slice_list(lst, start, end):
    if 0 <= start <= end <= len(lst):
        return lst[start:end]
    return "Invalid slice range."


def main():
    # Initial list
    my_list = ["apple", 42, "banana", 7.5, "grape"]

    print("Welcome to the List Game!")
    print("Your list:", my_list)

    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            idx = int(input("Enter index to access: "))
            print(access_element(my_list, idx))

        elif choice == "2":
            idx = int(input("Enter index to modify: "))
            new_val = input("Enter new value: ")
            print(modify_element(my_list, idx, new_val))

        elif choice == "3":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(my_list, start, end)
            print("Sliced list:", result)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again!")

        print("Current list:", my_list)


if __name__ == "__main__":
    main()
