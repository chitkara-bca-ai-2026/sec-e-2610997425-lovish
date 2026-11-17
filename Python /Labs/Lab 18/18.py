def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


while True:
    print("\n1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        n = int(input("Enter a non-negative integer: "))
        if n < 0:
            print("Error: Please enter a non-negative integer.")
        else:
            print(f"Factorial of {n} is {factorial(n)}")

    elif choice == "2":
        terms = int(input("Enter number of terms: "))
        if terms <= 0:
            print("Error: Please enter a positive number of terms.")
        else:
            series = []
            for i in range(terms):
                series.append(fibonacci(i))
            print("Fibonacci series:", *series)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1 to 3.")