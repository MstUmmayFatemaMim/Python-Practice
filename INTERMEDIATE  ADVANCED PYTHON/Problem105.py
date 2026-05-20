# ############    105. Mutable Inside Immutable
# Create a tuple containing:
# an integer
# a list
# Modify the list and explain why it works.
# Create a tuple with an immutable integer and a mutable list
my_tuple = (42, [1, 2, 3],8,9,[9,6,0])

print("Before modification:", my_tuple)
# Output: Before modification: (42, [1, 2, 3])

# Modify the list inside the tuple
my_tuple[1].append(4)
my_tuple[1].append(0)
my_tuple[1].append(9)
my_tuple[1].append(3)
print("After modification :", my_tuple)
