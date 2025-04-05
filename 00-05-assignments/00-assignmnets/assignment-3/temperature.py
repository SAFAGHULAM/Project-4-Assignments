# this programme will convert farehiet to celsius.

def main():
    input_fahrenheit = input("Enter the temperature in Fahrenheit: ")
    fahrenheit = float(input_fahrenheit)
    # formula to convert fahrenheit to celsius
    degrees_celsius = (fahrenheit - 32) * 5.0/9.0
    # printing the converted temperature
    output = "Temperature: " + str(fahrenheit) + "F = " + str(degrees_celsius) + "C"
    print(output)
    
if __name__ == "__main__":
    main()