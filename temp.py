# Design the program to take in temperature
def get_temperature():
    while True:
        try:
            temperature = float(input("Enter the temperature: "))
            return temperature
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Implement the temperature conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        print("Choose conversion direction:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            celsius = get_temperature()
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit}°F\n")
        elif choice == '2':
            fahrenheit = get_temperature()
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius}°C\n")
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
