# This is a simple Python program that asks for the user's name and then greets them.
name = input ("What is your name? ")

name = input ("What is your name? ").strip().title() # This line combines the input, strip, and title functions in one line to ensure that the name is both clean and properly formatted.

name = name.strip() # This line removes any leading or trailing whitespace from the user's input.
#this function is used to ensure that the name is clean and does not contain any extra spaces that could affect the output.

name = name.capitalize() # This line capitalizes the first letter of the user's name and makes the rest lowercase.
# This function is used to ensure that the name is properly formatted, regardless of how the user entered it (e.g., "john", "JOHN", "jOhN" will all be converted to "John").

name = name.title() # This line converts the user's name to title case, which means that the first letter of each word is capitalized.
# This function is used to ensure that the name is properly formatted, especially if the user entered multiple words (e.g., "john doe" will be converted to "John Doe").

name = name.strip().title() # This line combines the strip and title functions in one line to ensure that the name is both clean and properly formatted.

first, last = name.split(" ") # This line splits the user's name into two parts (first and last) based on the space character.
# This function is used to separate the first and last name, which can be useful for further processing or for personalized greetings.

print ("Hello, " + name)
print ("Hello,", name) # This is another way to print the greeting using a comma instead of concatenation.
print (f"Hello, {name}") # This is yet another way to print the greeting using an f-string.
# The program will output the greeting in three different ways, but all will include the user's name.

print (f"Hello, {first}") # This line uses an f-string to greet the user by their first name only, which can make the greeting feel more personal.
print (f"Hello, {last}") # This line uses an f-string to greet the user by their last name only, which can make the greeting feel more personal.