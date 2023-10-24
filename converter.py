def temperature_converter():
    print("Temperature Converter: Celsius <-> Fahrenheit")
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def length_converter():
    print("Length Converter: Meters <-> Feet")
    try:
        meters = float(input("Enter length in meters: "))
        feet = meters * 3.281
        print(f"{meters} meters is equal to {feet} feet.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def weight_converter():
    print("Weight Converter: Kilograms <-> Pounds")
    try:
        kilograms = float(input("Enter weight in kilograms: "))
        pounds = kilograms * 2.205
        print(f"{kilograms} kilograms is equal to {pounds} pounds.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def main():
    print("Welcome to the Unit Converter!")
    print("Choose an option:")
    print("1. Temperature Converter")
    print("2. Length Converter")
    print("3. Weight Converter")

    choice = input("Enter the number of your choice (1/2/3): ")

    if choice == '1':
        temperature_converter()
    elif choice == '2':
        length_converter()
    elif choice == '3':
        weight_converter()
    else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
