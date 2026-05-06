def main():
    print("Welcome to the unit converter!")
    print("Select one of the availabe converting operations: ")
    print("1. Celsius to Fahrenheit")
    print("2. Kilometers to Miles")
    print("3. Dollars to Lempiras")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F.")
    elif choice == "2":
        kilometers = float(input("Enter the kilometers amount: "))
        miles = kilometers_to_miles(kilometers)
        print(f"{kilometers} kilometers is equal to {miles} miles.")
    elif choice == "3":
        dollars = float(input("Enter the dollars quantity: "))
        lempiras = dollars_to_lempiras(dollars)
        print(f"{dollars} dollars is equal to {lempiras} lempiras.")
    else:
        print("Invalid choice.")


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32        

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def dollars_to_lempiras(dollars):
    return dollars * 26.5

main()