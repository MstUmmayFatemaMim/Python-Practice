########        Build a simple contact book using dictionary.

import csv
import os

# Your specific file path
FILE_PATH = r"C:\Users\Mim\Downloads\contact(Sheet1).csv"
# Load previous data from your CSV file immediately
contacts = {}
if os.path.exists(FILE_PATH):
    # with open(FILE_PATH, "r", newline="", encoding="utf-8") as f:
    #     # Converts rows directly into the contacts dictionary
    #     contacts = dict(csv.reader(f))
    with open(FILE_PATH, "r", newline="", encoding="utf-8") as f:
        # Loop through each row and only add it if it is not empty
        for row in csv.reader(f):
            if row:  # This skips completely blank lines
                contacts[row[0]] = row[1]



def add_contact():
    name = input("Enter name  : ")
    phone = input("Enter phone : ")
    if name in contacts:
        print(f"'{name}' already exists!")
    elif phone in contacts.values():  # CHECK FOR DUPLICATE PHONE NUMBER
        print(f"The phone number '{phone}' is already assigned to another contact!")
    else:
        contacts[name] = phone

        # Save new contact straight to your CSV file
        with open(FILE_PATH, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([name, phone])

        print(f"{name}, {phone} added successfully!")


def view_contacts():
    if not contacts:
        print("Your contact book is empty!")
        return

    print("\n--- Saved Contacts ---")
    for name, phone in contacts.items():
        print(f"Name: {name} | Phone: {phone}")


def update_contact():
    if not contacts:
        print("Your contact book is empty!")
        return

    # 1. Ask which contact the user wants to update
    old_name = input("Enter the name of the contact you want to update: ").strip()

    if old_name not in contacts:
        print(f"'{old_name}' does not exist!")
        return

    # 2. Ask what they want to change
    print("\nWhat do you want to update?")
    print("1. Update Name")
    print("2. Update Phone Number")
    sub_choice = input("Choose an option (1 or 2): ").strip()

    match sub_choice:
        case "1":
            new_name = input("Enter the new name: ").strip()
            if new_name in contacts:
                print(f"Error: '{new_name}' already exists in your contacts!")
                return
            # Swap the old key for the new key in the dictionary
            phone = contacts.pop(old_name)
            contacts[new_name] = phone
            print(f"Name successfully updated from '{old_name}' to '{new_name}'!")

        case "2":
            new_phone = input("Enter the new phone number: ").strip()
            # Update the phone number value
            contacts[old_name] = new_phone
            print(f"Phone number for '{old_name}' successfully updated to '{new_phone}'!")

        case _:
            print("Invalid option. Returning to main menu.")
            return

    # 3. Save the updated dictionary back to your CSV file
    with open(FILE_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for k, v in contacts.items():
            writer.writerow([k, v])


def delete_contact():
    if not contacts:
        print("Your contact book is empty!")
        return

    name = input("Enter the name of the contact you want to delete: ").strip()

    if name in contacts:
        # Remove the contact from the dictionary
        del contacts[name]

        # Rewrite the CSV file without the deleted contact
        with open(FILE_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for k, v in contacts.items():
                writer.writerow([k, v])

        print(f"'{name}' deleted successfully!")
    else:
        print(f"'{name}' does not exist!")


def search_contact():
    # 1. SAFETY CHECK
    if not contacts:
        print("Your contact book is empty!")
        return

    # 2. CAPTURE USER SEARCH INPUT
    query = input("Enter the name or phone number to search: ").strip()
    found = False  # Track if we find anything

    print("\n--- Search Results ---")

    # 3. THE LOOP MECHANISM
    for name, phone in contacts.items():
        # Check if what they typed matches the Name OR the Phone number
        if query == name or query == phone:
            print(f"Name: {name} | Phone: {phone}")
            found = True

    # 4. FALLBACK CHECK
    if not found:
        print(f"No contact found matching '{query}'.")


def showlist():
    print("\n***** Contact Book ******")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. View Contacts")
    print("0. Exit")
    print("*************************")


while True:
    showlist()
    choice = input("Choose an option: ")

    match choice:
        case "1":
            add_contact()
        case '2':
            update_contact()
        case '3':
            search_contact()
        case '4':
            delete_contact()
        case "5":
            view_contacts()
        case "0":
            print("Goodbye!")
            break
        case _:
            print("Invalid option, try again.")
