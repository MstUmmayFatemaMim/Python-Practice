#Write a function that accidentally modifies a list.
def _mlist(x):
    x.append(99)
    return x
y=[4,6,8,9]
_mlist(y)
print(y)

# ####Way 2 — extend() adds multiple items
# def _mlist(x):
#     x.extend([99, 100])   # adds multiple items in place
#     return x
#
# y = [4, 6, 8, 9]
# _mlist(y)
# print(y)   # [4, 6, 8, 9, 99, 100]  😱 modified!
#########.extend() also works in place — same problem as .append() but adds multiple items at once.

# ###########Way 3 — insert() at specific position
# def _mlist(x):
#     x.insert(0, 99)   # inserts 99 at index 0
#     return x
#
# y = [4, 6, 8, 9]
# _mlist(y)
# print(y)   # [99, 4, 6, 8, 9]  😱 modified!
#########.insert() shifts all elements and modifies the original list in place.

######Way 4 — remove() deletes from original
# def _mlist(x):
#     x.remove(x[3])    # removes first occurrence of 4
#     return x
#
# y = [4, 6, 8, 9]
# _mlist(y)
# print(y)   # [6, 8, 9]  😱 modified!
# #####.remove() deletes directly from the original — y permanently loses the value 4.
#
# #####Way 5 — pop() removes and returns item
# def _mlist(x):
#     popped = x.pop(2)   # removes last item give only index number
#     return popped
#
# y = [4, 6, 8, 9]
# _mlist(y)
# print(y)   # [4, 6, 8]  😱 modified! 9 is gone!
# #######.pop() removes from the original list — y loses its last element permanently.
#
# ########Way 6 — direct index assignment
# def _mlist(x):
#     x[0] = 99     # changes index 0 of original
#     return x
#
# y = [4, 6, 8, 9]
# _mlist(y)
# print(y)   # [99, 6, 8, 9]  😱 modified!
# ######x[0] = 99 reaches directly into the original list and replaces the value. No new list created at all.
#
# ######Way 7 — slice assignment
# def _mlist(x):
#     x[1:3] = [99, 100]   # replaces index 1 and 2
#     return x
#
# y = [4, 6, 8, 9]
# _mlist(y)
# print(y)   # [4, 99, 100, 9]  😱 modified!
# #####Slice assignment modifies the list in place — replaces a range of elements in the original.
#
# #########Way 8 — sort() and reverse() in place
# def _mlist(x):
#     x.sort()      # sorts original in place
#     return x
#
# y = [9, 4, 8, 6]
# _mlist(y)
# print(y)   # [4, 6, 8, 9]  😱 original sorted!
#
# def _mlist2(x):
#     x.reverse()   # reverses original in place
#     return x
#
# _mlist2(y)
# print(y)   # [9, 8, 6, 4]  😱 original reversed!
# ########Both .sort() and .reverse() work in place — they permanently change the original list order.
#
# ######Way 9 — nested list inside modified through function
# def _mlist(x):
#     x[0].append(99)   # modifies inner list of original
#     return x
#
# y = [[1, 2], [3, 4]]
# _mlist(y)
# print(y)   # [[1, 2, 99], [3, 4]]