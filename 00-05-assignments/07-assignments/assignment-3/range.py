def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True

    # No need for an 'else' because we are already returning
    return False

# Example calls to the function and printing the results
print(in_range(5, 1, 10))  # Output: True
print(in_range(0, 1, 10))  # Output: False
print(in_range(10, 1, 10)) # Output: True
