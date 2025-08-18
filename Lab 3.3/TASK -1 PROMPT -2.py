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

def main():
    print("=== FACTORIAL CALCULATOR ===")
    
    while True:
        try:
            # Get user input
            user_input = input("\nEnter a number to calculate factorial (or 'quit' to exit): ")
            
            # Check if user wants to quit
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            # Convert input to integer
            number = int(user_input)
            
            # Calculate factorial
            result = factorial(number)
            
            # Display result
            if isinstance(result, str):
                print(f"Result: {result}")
            else:
                print(f"Factorial of {number} = {result}")
                print(f"({number}! = {result})")
                
        except ValueError:
            print("Error: Please enter a valid integer!")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break

if __name__ == "__main__":
    main()
