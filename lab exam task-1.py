def factorial_febo(n: int) -> None:
    if not isinstance(n, int) or n < 0:
        print("Please provide a non-negative integer.")
        return

    # Factorial of n
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i

    # Fibonacci series of n terms
    fibonacci = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci.append(a)
        a, b = b, a + b

    print(f"Factorial of {n}: {factorial}")
    print(f"Fibonacci series ({n} terms): {', '.join(map(str, fibonacci))}")


# Example usage:
if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        factorial_febo(num)
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")