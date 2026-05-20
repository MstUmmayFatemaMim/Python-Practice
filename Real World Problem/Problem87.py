##########      Build a shopping cart where items can be added/removed.

# Shopping_cart={
#     "Pen" : 50,
#     "Pencil" : 10,
#     "Notebook" : 500
# }
# print(Shopping_cart)
#
# Shopping_cart["Bag"]=100
# print(Shopping_cart)
# print(Shopping_cart.keys())


import csv
import os

FILE_PATH=r"C:\Users\Mim\Downloads\ShoppingList(Sheet1).csv"

card={}
if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r", newline="", encoding="utf-8") as f:       ###### Read the file
        # card=dict(csv.reader(f))
        for row in csv.reader(f):
            if len(row) == 2:  # skip empty or malformed rows
                card[row[0]] = row[1]
print("Loaded card:", card)

def add_items():
    product=input("Enter product : ")
    price=input("Enter price : ")
    if product in card:
        print(f"Item {product} already added.")
    else:
        card[product]=price
        with open(FILE_PATH, "a", newline="", encoding="utf-8") as f:       ### append the new things
            csv.writer(f).writerow([product,price])

        print(f"Item {product} ,{price}added successfully.")


def delete_item():
    if not card:
        print("Your card is empty!")
        return

    product = input("Enter the name of the product you want to delete: ").strip()

    if product in card:
        # Remove the card from the dictionary
        del card[product]

        # Rewrite the CSV file without the deleted product
        with open(FILE_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for k, v in card.items():
                writer.writerow([k, v])

        print(f"'{product}' deleted successfully!")
    else:
        print(f"'{product}' does not exist!")




def showlist():
    print("\n***** Contact Book ******")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("0. Exit")
    print("*************************")

while True:
    showlist()
    choice=input("Enter your choice: ")
    if choice=="1":
        add_items()
    elif choice=="2":
        delete_item()
    elif choice=="0":
        print("Goodbye")
        break
    else:
        print("Invalid option. Returning to main menu.")
