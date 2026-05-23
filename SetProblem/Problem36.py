# #########   Add multiple elements to a set.
# set1 = {1, 2}
# set2= {3, 4}
# newset = set1 | set2
# print(newset)

# myset = {2,3,5,7,8,1,9}
# print(myset.update([99,88,66,55,33]))     ########## it works but print None

myset = {2, 3, 5, 7, 8, 1, 9}

# 1. Update the set first (this happens in-place)
myset.update([99, 88, 66, 55, 33])

# 2. Print the set after it has been changed
print(myset)

