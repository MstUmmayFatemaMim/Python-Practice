# #############       111. Multi-Level Reference Problem
# Predict and then write code to verify:
# a = [[1, 2], [3, 4]]
# b = a.copy()
# c = a[:]
# Modify one inner list and explain all variables.

# Initialize the original 2D list
a = [[1, 2], [3, 4]]

# Perform two different types of shallow copies
b = a.copy()
c = a[:]

# Modify the first inner list via variable 'a'
a[0].append(99)

# Print the results
print("a:", a)  # Output: [[1, 2, 99], [3, 4]]
print("b:", b)  # Output: [[1, 2, 99], [3, 4]]
print("c:", c)  # Output: [[1, 2, 99], [3, 4]]
