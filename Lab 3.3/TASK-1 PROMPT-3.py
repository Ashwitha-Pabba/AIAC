def factorial_iterative(n):
    """
    Calculate factorial using iterative approach
    """
    if n < 0:
        return "Error: Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """
    Calculate factorial using recursive approach
    """
    if n < 0:
        return "Error: Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursive(n - 1)

def factorial_math_module(n):
    """
    Calculate factorial using Python's math module
    """
    import math
    if n < 0:
        return "Error: Factorial is not defined for negative numbers"
    return math.factorial(n)

def main():
    print("=== Factorial Calculator ===")
    print("Choose calculation method:")
    print("1. Iterative approach")
    print("2. Recursive approach")
    print("3. Using math module")
    print("4. All methods comparison")
    
    try:
        choice = int(input("\nEnter your choice (1-4): "))
        n = int(input("Enter a number to calculate factorial: "))
        
        if choice == 1:
            result = factorial_iterative(n)
            print(f"\nFactorial of {n} (Iterative): {result}")
            
        elif choice == 2:
            result = factorial_recursive(n)
            print(f"\nFactorial of {n} (Recursive): {result}")
            
        elif choice == 3:
            result = factorial_math_module(n)
            print(f"\nFactorial of {n} (Math module): {result}")
            
        elif choice == 4:
            print(f"\n=== Factorial of {n} using all methods ===")
            print(f"Iterative: {factorial_iterative(n)}")
            print(f"Recursive: {factorial_recursive(n)}")
            print(f"Math module: {factorial_math_module(n)}")
            
        else:
            print("Invalid choice! Please select 1-4.")
            
    except ValueError:
        print("Error: Please enter valid integers!")
    except RecursionError:
        print("Error: Number too large for recursive method!")

if __name__ == "__main__":
    main()
