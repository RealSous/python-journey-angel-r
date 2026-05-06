def main ():
    print ("Welcome to the advanced calculator!")
    print("Insert X and Y to perform calculations.")
    x = float(input("Insert X: "))
    y = float(input("Insert Y: "))

    print("These are all the operations results: ")
    print(f"Addition: {add(x, y)}")
    print(f"Subtraction: {substract(x, y)}")
    print(f"Multiplication: {multiply(x, y)}")
    print(f"Division: {divide(x, y)}")

def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

main()