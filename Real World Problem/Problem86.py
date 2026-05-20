#########   Build a simple contact book using dictionary.

# contacts = {
#     "Alice": "555-0101",
#     "Bob": "555-0202"
# }
# ## Add
# contacts["Charlie"] = "555-0303"
# print(contacts)
# ### Search
# print(contacts.get("Alice"))        ######## Found --> Id print
# ##### Delete
# del contacts["Bob"]
# print(contacts)
# ### Search
# print(contacts.get("Bob"))      ####### Not found -->None


contact={}
def showlist():
    print(" *****   contact     ******")
    print("Add Contact")
    print("Update Contact")
    print("Delete Contact")
    print("Show All Contact")

print(showlist())