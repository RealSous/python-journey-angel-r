# This program is a simple calculator that takes two numbers as input and outputs their sum.
x = input ("What is x? ")
y = input ("What is y? ")

z = int(x) + int(y)

print (z)




# This is a more concise version of the calculator program that combines the input and conversion to integers in one line.
x = int(input ("What is x? "))
y = int(input ("What is y? "))

print (x + y)




 # This line combines the input, conversion to integers, and addition in one line for a more concise version of the calculator program.
print (int(input ("What is x? ")) + int(input ("What is y? ")))




# This version of the calculator program uses floats instead of integers, which allows for decimal numbers to be added together.
x = float(input ("What is x? "))
y = float(input ("What is y? "))

print (x + y)




print(round(x + y)) # This line rounds the result of the addition to the nearest whole number.

z = round(x + y) # This line rounds the result of the addition and stores it in a variable called z.
print (z) # This line prints the rounded result stored in the variable z.


print (f"{z:,}") # This line uses an f-string to format the output with a comma as a thousands separator, which can make large numbers easier to read.



x = float(input ("What is x? "))
y = float(input ("What is y? "))

z = round(x + y, 2) # This line rounds the result of the addition to 2 decimal places, which can be useful for financial calculations or when working with measurements that require precision.
print (z)


print (f"{z:.2f}") # This line uses an f-string to format the output with 2 decimal places, which can be useful for financial calculations or when working with measurements that require precision.
