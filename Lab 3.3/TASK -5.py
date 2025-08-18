def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, from_unit, to_unit):
    """
    Convert temperature from one unit to another
    
    Args:
        value (float): Temperature value to convert
        from_unit (str): Source unit ('C', 'F', 'K')
        to_unit (str): Target unit ('C', 'F', 'K')
    
    Returns:
        float: Converted temperature value
    """
    
    # First convert to Celsius as intermediate step
    if from_unit.upper() == 'C':
        celsius = value
    elif from_unit.upper() == 'F':
        celsius = fahrenheit_to_celsius(value)
    elif from_unit.upper() == 'K':
        celsius = kelvin_to_celsius(value)
    else:
        raise ValueError(f"Invalid source unit: {from_unit}")
    
    # Then convert from Celsius to target unit
    if to_unit.upper() == 'C':
        return celsius
    elif to_unit.upper() == 'F':
        return celsius_to_fahrenheit(celsius)
    elif to_unit.upper() == 'K':
        return celsius_to_kelvin(celsius)
    else:
        raise ValueError(f"Invalid target unit: {to_unit}")

def display_conversion_table(celsius_value):
    """Display conversion table for a given Celsius value"""
    fahrenheit = celsius_to_fahrenheit(celsius_value)
    kelvin = celsius_to_kelvin(celsius_value)
    
    print(f"\n=== TEMPERATURE CONVERSION TABLE ===")
    print(f"Input: {celsius_value}°C")
    print("-" * 40)
    print(f"Celsius:    {celsius_value:8.2f}°C")
    print(f"Fahrenheit: {fahrenheit:8.2f}°F")
    print(f"Kelvin:     {kelvin:8.2f}K")
    print("=" * 40)

def get_temperature_scale_info():
    """Display information about different temperature scales"""
    print("\n=== TEMPERATURE SCALES INFORMATION ===")
    print("Celsius (°C):")
    print("  - Water freezes at 0°C")
    print("  - Water boils at 100°C")
    print("  - Room temperature: ~20-25°C")
    print("  - Body temperature: 37°C")
    
    print("\nFahrenheit (°F):")
    print("  - Water freezes at 32°F")
    print("  - Water boils at 212°F")
    print("  - Room temperature: ~68-77°F")
    print("  - Body temperature: 98.6°F")
    
    print("\nKelvin (K):")
    print("  - Absolute zero: 0K")
    print("  - Water freezes at 273.15K")
    print("  - Water boils at 373.15K")
    print("  - Room temperature: ~293-298K")
    print("  - Body temperature: 310.15K")

def main():
    """Main program loop"""
    print("=== TEMPERATURE CONVERTER ===")
    print("Convert temperatures between Celsius, Fahrenheit, and Kelvin")
    
    while True:
        print("\nChoose an option:")
        print("1. Convert temperature")
        print("2. Show conversion table")
        print("3. Temperature scale information")
        print("4. Quick conversions")
        print("5. Exit")
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                # Single temperature conversion
                print("\n--- TEMPERATURE CONVERSION ---")
                
                # Get input value and unit
                try:
                    value = float(input("Enter temperature value: "))
                except ValueError:
                    print("Error: Please enter a valid number!")
                    continue
                
                print("\nAvailable units: C (Celsius), F (Fahrenheit), K (Kelvin)")
                from_unit = input("Enter source unit (C/F/K): ").strip().upper()
                to_unit = input("Enter target unit (C/F/K): ").strip().upper()
                
                try:
                    result = convert_temperature(value, from_unit, to_unit)
                    print(f"\n✓ {value}°{from_unit} = {result:.2f}°{to_unit}")
                except ValueError as e:
                    print(f"✗ Error: {e}")
            
            elif choice == '2':
                # Conversion table
                print("\n--- CONVERSION TABLE ---")
                try:
                    celsius_input = float(input("Enter temperature in Celsius: "))
                    display_conversion_table(celsius_input)
                except ValueError:
                    print("Error: Please enter a valid number!")
            
            elif choice == '3':
                # Temperature scale information
                get_temperature_scale_info()
            
            elif choice == '4':
                # Quick common conversions
                print("\n--- QUICK CONVERSIONS ---")
                print("Common temperature conversions:")
                
                # Predefined conversions
                conversions = [
                    (0, 'C', 'F', "Freezing point of water"),
                    (100, 'C', 'F', "Boiling point of water"),
                    (37, 'C', 'F', "Body temperature"),
                    (25, 'C', 'F', "Room temperature"),
                    (0, 'C', 'K', "Freezing point of water"),
                    (100, 'C', 'K', "Boiling point of water"),
                    (32, 'F', 'C', "Freezing point of water"),
                    (212, 'F', 'C', "Boiling point of water"),
                    (98.6, 'F', 'C', "Body temperature"),
                    (273.15, 'K', 'C', "Freezing point of water"),
                    (373.15, 'K', 'C', "Boiling point of water")
                ]
                
                for value, from_unit, to_unit, description in conversions:
                    try:
                        result = convert_temperature(value, from_unit, to_unit)
                        print(f"{value}°{from_unit} = {result:.2f}°{to_unit} ({description})")
                    except ValueError:
                        continue
                
                print("\n--- CUSTOM QUICK CONVERSION ---")
                try:
                    quick_value = float(input("Enter temperature: "))
                    quick_from = input("From unit (C/F/K): ").strip().upper()
                    quick_to = input("To unit (C/F/K): ").strip().upper()
                    
                    quick_result = convert_temperature(quick_value, quick_from, quick_to)
                    print(f"✓ {quick_value}°{quick_from} = {quick_result:.2f}°{quick_to}")
                    
                except ValueError:
                    print("Error: Please enter valid values!")
            
            elif choice == '5':
                print("Thank you for using Temperature Converter!")
                break
            
            else:
                print("Invalid choice! Please select 1-5.")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
