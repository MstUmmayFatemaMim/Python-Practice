# # ###########     120. Design a Safe API
# # Design a small module with:
# # One function that returns internal data safely
# # One function that modifies internal data
# #  Prevent accidental corruption by the user.
# # "C:\Users\Mim\Downloads\Data.xlsx"
#
contacts = []

def add_contact(name, phone):
    contacts.append({"name": name, "phone": phone})
    print(f"{name} {phone} - Contact added successfully!")

add_contact("mim", "9087")
add_contact("ali", "1234")
print(contacts)

def get_contact():
    return contacts
get_contact()
print("View all data {contacts}")
print(contacts)


def delete_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print(f"{name} - Contact deleted successfully!")
            return contact
    print(f"{name} not found!")

delete_contact("ali")
delete_contact("mimi")
print(contacts)
