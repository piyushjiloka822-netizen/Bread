def celsius_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    Formula: F = (C * 9/5) + 32
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# Example usage:
celsius_val = 25
result = celsius_to_fahrenheit(celsius_val)
print(f"{celsius_val}°C is equal to {result}°F")