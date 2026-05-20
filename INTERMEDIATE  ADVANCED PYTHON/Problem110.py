# ########    110. Hashing & Mutability
# Create:
# A tuple containing a list
# Attempt to use it as a dictionary key
# Fix the issue and explain why it works

# 1. Start with the broken tuple (It has a list trapped inside)
broken_key = (1, 2, [3, 4])

# 2. Extract the items directly using index positions
item1 = broken_key[0]  # Gets the number 1
item2 = broken_key[1]  # Gets the number 2
inner_list = broken_key[2]  # Gets the list [3, 4]

# 3. THE FIX: Convert that specific list into a tuple
frozen_inner_item = tuple(inner_list)  # Turns into (3, 4)

# 4. REBUILD: Put them all back together as a 100% frozen tuple
fixed_key = (item1, item2, frozen_inner_item)  # Becomes (1, 2, (3, 4))

# 5. USE IT: This works perfectly as a dictionary key!
my_dictionary = {}
my_dictionary[fixed_key] = "Successfully Stored!"

print(my_dictionary)
# Output: {(1, 2, (3, 4)): 'Successfully Stored!'}



