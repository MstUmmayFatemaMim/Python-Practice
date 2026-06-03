##############  Merge two lists without using +.
list1 = [1, 3, 6, 4, 9]
list2 = ['a', 'g', 'y']
for i in list1:
    list2.append(i)
print(list2)

list1 = [1, 3, 6, 4, 9]
list2 = ['a', 'g', 'y']

# Unpack both lists into a new list
merged = [*list1, *list2]

print(merged)
# Output: [1, 3, 6, 4, 9, 'a', 'g', 'y']

list1 = [1, 3, 6, 4, 9]
list2 = ['a', 'g', 'y']

# Create a copy of list1 so you don't destroy your original data
merged = list1.copy()
merged.extend(list2)

print(merged)
# Output: [1, 3, 6, 4, 9, 'a', 'g', 'y']

list1 = [1, 3, 6, 4, 9]
list2 = ['a', 'g', 'y']

# Make a copy of list1
merged = list1[:]
# Assign list2 to an empty slice at the very end of the list
merged[len(merged):] = list2

print(merged)
# Output: [1, 3, 6, 4, 9, 'a', 'g', 'y']

from itertools import chain

list1 = [1, 3, 6, 4, 9]
list2 = ['a', 'g', 'y']

# Chain them together and convert the result back to a list
merged = list(chain(list1, list2))

print(merged)
# Output: [1, 3, 6, 4, 9, 'a', 'g', 'y']
