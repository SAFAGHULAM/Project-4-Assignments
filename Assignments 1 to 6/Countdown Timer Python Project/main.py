import time

def countdown_timer():
    # Get input from the user for countdown time in seconds
    try:
        countdown_time = int(input("Enter countdown time in seconds: "))
    except ValueError:
        print("Please enter a valid number!")
        return
    
    print(f"Starting countdown from {countdown_time} seconds...")

    # Countdown loop
    while countdown_time > 0:
        print(countdown_time, "seconds remaining...")
        time.sleep(1)  # Wait for 1 second
        countdown_time -= 1

    print("Time's up!")

# Start the countdown timer
countdown_timer()
