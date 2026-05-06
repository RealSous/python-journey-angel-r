def main ():

    item = input("Enter the item name: ")
    item = item.strip().title()
    item_price = float(input("Enter the item price: "))
    quantity = int(input("Enter the quantity: "))

    print("===== RECEIPT =====")
    print(f"Item: {item}")
    print(f"Price: ${item_price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${item_price * quantity:.2f}")


main()    