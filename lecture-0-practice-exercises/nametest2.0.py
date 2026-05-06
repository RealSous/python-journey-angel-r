def main():
    name = input("Please enter your name: ")
    name = name.strip().title()

    first, last, = name.split(" ")[0], name.split(" ")[-1]

    print(f"First Name: {first}")
    
    print(f"Last Name: {last}")
    

main()    
