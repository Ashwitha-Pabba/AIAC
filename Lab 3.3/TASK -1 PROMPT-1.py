def factorial(n):
    """
    Calculate factorial of a number
    """
    if n < 0:
        return "Error: Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
if __name__ == "__main__":
    # Test with different numbers
    test_numbers = [0, 1, 5, 10]
    
    for num in test_numbers:
        result = factorial(num)
        print(f"Factorial of {num} = {result}")
    
    # Interactive input
    try:
        user_input = int(input("\nEnter a number to calculate factorial: "))
        result = factorial(user_input)
        print(f"Factorial of {user_input} = {result}")
    except ValueError:
        print("Error: Please enter a valid integer!")
