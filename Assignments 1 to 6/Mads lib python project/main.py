print("Welcome to the Mad Libs Game!")

# Asking for inputs
noun = input("Enter a noun: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")

# Mad Libs story template
story = f"""
Once upon a time, there was a {adjective} {noun} who loved to {verb}.
Every day, it would go to {place} and make everyone laugh.
The end!
"""

# Output the final story
print("\nHere is your Mad Libs story:")
print(story)
