def main():
    x = int(input ("What is x? "))
    print ("X squared is", square(x)) # This line calculates the square of x and prints the result in a formatted string.

def square(n):

    #This is one way to sqyuare a number, by multiplying it by itself.
    return n * n
    # This is another way to square a number, by using the exponentiation operator (**).
    return n ** 2
    # This is yet another way to square a number, by using the built-in pow() function.
    return pow(n, 2)




main()