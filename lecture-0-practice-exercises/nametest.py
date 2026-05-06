def main():
    name = input("Please enter your full name: ")
    name = name.strip().title()
    name_length = len(name)

    print(f"Hello, {name}!")
    print(f"Your name has {name_length} characters.")

main()    