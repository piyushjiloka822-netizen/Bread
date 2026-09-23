def calculate_factorial(n):
    # Handle negative inputs if necessary
    if n < 0:
        return "Factorial is not defined for negative numbers"
        
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
print(calculate_factorial(5))  # Output: 120