# #Show tuple containing a list and modify the list.
# # Tuple is IMMUTABLE — you cannot change its elements
# t = (1, 2, 3)
# t[0] = 99      # ❌ TypeError: tuple does not support item assignment

################Method 1 — append() add one item
# t = (1, [2, 3], [4,5],6,9,[4,9])
# t[5].append(99)         #t[1] accesses the list inside the tuple
#                         # .append() adds one item to the end of that list.
#                         #The tuple wrapper never changes — only the list contents change.
# print(t)        #(1, [2, 3, 99], 4)

##########prove with id() tuple never changed
t = (1, [2, 3], 4)

print(id(t))      # e.g. 140234567   ← tuple address
print(id(t[1]))   # e.g. 140234891   ← list address
print(t)
t[1].append(99)

print(id(t))      # 140234567  ← SAME! tuple unchanged ✅
print(id(t[1]))   # 140234891  ← SAME! same list object ✅
print(t)          # (1, [2, 3, 99], 4)

# #################Method 2 — extend() add multiple items
# t = (1, [2, 3], 4)
# t[1].extend([10, 20, 30])           #####.extend() unpacks an iterable and adds all its items to the list at once.
# print(t)

###############Method 3 — insert() add at specific position
# t = (1, [2, 3], 4)
# t[1].insert(0, 99)   # insert 99 at index 0  -->.insert(index, value)
# print(t)  # (1, [99, 2, 3], 4)      #### It puts a new item at exactly the position you choose. Everything else shifts right.

###################Method 4 — remove() delete by value
# t = (1, [2, 3, 99], 4)
# t[1].remove(3)       # remove(value) searches for the value and deletes its first occurrence from the list.
#                     # Throws ValueError if not found
# print(t)  # (1, [2, 99], 4)

# ##########Method 5 — pop() remove by index
# t = (1, [2, 3, 99], 4)
# removed = t[1].pop(0)   # remove item at index 0 ***********.pop(index) removes and returns the item at that index.
#                         # Without an index, it removes the last item.
# print(removed)           # 2
# print(t)

# #############Method 6 — direct index assignment
# t = (1, [2, 3, 4], 5)
# t[1][0] = 99     # t[1][0] means: go to t[1] (the list), then go to index [0] of that list. You're changing a list element — not the tuple.
# print(t)  # (1, [99, 3, 4], 5)
#
#
# #########################Method 7 — slice assignment replace multiple items
# t = (1, [2, 3, 4, 5], 6)  ######Slice assignment replaces a range of items inside the list with new values. Very powerful — can even replace different lengths.
# t[1][1:3] = [30, 40]    # replace index 1 and 2
# print(t)  # (1, [2, 30, 40, 5], 6)

###########################Method 8 — sort() and reverse() in place
# t = (1, [5, 2, 8, 1, 3], 6)
# t[1].sort()       # sort the inner list in place
# print(t)          # (1, [1, 2, 3, 5, 8], 6)
# t[1].reverse()    # reverse the inner list in place
# print(t)          # (1, [8, 5, 3, 2, 1], 6)