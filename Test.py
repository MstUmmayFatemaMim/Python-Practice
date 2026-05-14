# fruits = ["apple", "banana", "mango"]
# # print(fruits[0])  # Output: apple (first item)
# # print(fruits[1])  # Output: banana
# print(fruits[-1])  # Output: mango (last item, negative index)

# Rahim’s Simple Fruit Inventory Tracker
fruits = []

while True:
    print("\nRahim’s Fruit Stall")
    print("1. Add a fruit")
    print("2. Remove a fruit")
    print("3. Show fruits")
    print("4. Done")

    choice = input("What do you want to do? (1-4): ")

    if choice == "1":
        fruit = input("Enter fruit name: ")
        fruits.append(fruit)
        print(f"{fruit} added to inventory!")

    elif choice == "2":
        fruit = input("Enter fruit to remove: ")
        if fruit in fruits:
            fruits.remove(fruit)
            print(f"{fruit} removed!")
        else:
            print(f"{fruit} not in inventory!")

    elif choice == "3":
        if fruits:
            print("Your fruits:", fruits)
            print("Total fruits:", len(fruits))
        else:
            print("No fruits in inventory!")

    elif choice == "4":
        print("Goodbye, Rahim! Happy selling!")
        break

    else:
        print("Please choose 1, 2, 3, or 4!")