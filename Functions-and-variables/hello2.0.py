# example of a function with a parameter and a default value
def hello(to="world"):
    print("hello,", to)

hello()
name = input("What is your name? ")
hello(name)



def main():
    hello()
    name = input("What is your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)

main()
