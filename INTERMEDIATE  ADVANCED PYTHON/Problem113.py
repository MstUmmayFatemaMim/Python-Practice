# 113. Hidden Bug in Loop
# Write buggy code where:
# Appending items to a list while iterating causes logical error
#  Then fix it.
# lst = [1, 2, 3]
# for x in lst:
#     if x == 2:
#         lst.remove(x)
#
# print(lst)
# lst = [1, 2, 3]


#############   iterate over a copy [:]
lst = [1, 2, 2, 3]

for x in lst[:]:         # loop over snapshot copy
    if x == 2:
        lst.remove(x)    # modify original safely

print(lst)

# #############   Fix 2 — list comprehension (most Pythonic)
# lst = [1, 2, 2, 3]
#
# lst = [x for x in lst if x != 2]
#
# print(lst)
#
# ########### Fix 3 — filter()
# lst = [1, 2, 2, 3]
#
# lst = list(filter(lambda x: x != 2, lst))       ####### condition,list
#
# print(lst)