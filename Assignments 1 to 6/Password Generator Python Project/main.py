import random
import string

def generate_password(length=12):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Randomly select characters from the combined set
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# Get the desired password length from the user
try:
    password_length = int(input("Enter the length of the password: "))
except ValueError:
    print("Please enter a valid number!")
    exit()

# Generate and display the password
password = generate_password(password_length)
print(f"Your generated password is: {password}")
