# ############    Find intersection of three lists.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]
def intersection(list1, list2, list3):
    result = []
    for item in list1:
        if item in list2 and item in list3:   # must exist in ALL lists
            result.append(item)
    return result
print(intersection(list1, list2, list3))

# ###############     Way 2 — Using set intersection (most popular)
# def intersection(list1, list2, list3):
#     return list(set(list1) & set(list2) & set(list3))
# print(intersection(list1, list2, list3))

# ##############      Way 3 — Using .intersection() method (most readable)
# def intersection(list1, list2, list3):
#     return list(set(list1).intersection(set(list2), set(list3)))
# print(intersection(list1, list2, list3))


# ##############  Way 4 — List comprehension (compact)
# def intersection(list1, list2, list3):
#     return [item for item in list1
#             if item in list2
#             and item in list3]
#
# print(intersection(list1, list2, list3))

# #########       Way 5 — Using *args (works with ANY number of lists)
# def intersection(*lists):
#     result = set(lists[0])              # start with first list
#     for lst in lists[1:]:              # loop remaining lists
#         result = result & set(lst)     # keep only common items
#     return list(result)
#
# # works with 2, 3, 4 or more lists!
# print(intersection(list1, list2))
# print(intersection(list1, list2, list3))
# print(intersection(list1, list2, list3, [5, 10, 11]))

# ##########      Way 6 — Using reduce (functional style, advanced)
# from functools import reduce
#
# def intersection(*lists):
#     return list(reduce(lambda a, b: set(a) & set(b), lists))
#
# print(intersection(list1, list2, list3))

# ###########     Way 7 — Using Counter (find items with exact frequency)
# from collections import Counter
#
# def intersection(*lists):
#     combined = Counter()
#     for lst in lists:
#         combined.update(set(lst))      # count how many lists each item appears in
#
#     total_lists = len(lists)
#     return [item for item, count in combined.items()
#             if count == total_lists]   # keep only items in ALL lists
#
# print(intersection(list1, list2, list3))