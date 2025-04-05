MAX_VALUE = 10000  # constant

def main():
    a = 0  # Fib(0)
    b = 1  # Fib(1)

    while a < MAX_VALUE:
        print(a, end=" ")  # print current term
        a, b = b, a + b     # update to next term (a becomes b, b becomes a + b)

if __name__ == '__main__':
    main()
