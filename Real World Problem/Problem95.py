#############   Create a function that returns unique elements from multiple lists.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

def get_unique(list1, list2, list3):
    combined = []
    for item in list1 + list2 + list3:   # merge all lists into one
        if item not in combined:          # check if already added
            combined.append(item)
    return combined

print(get_unique(list1, list2, list3))

# ######### Way 2 — Using set() (most popular)
# def get_unique(list1, list2, list3):
#     combined = list1 + list2 + list3     # merge all
#     return list(set(combined))           # set removes duplicates
#
# print(get_unique(list1, list2, list3))

# #######     Way 3 — Using set() but preserve order
# def get_unique(list1, list2, list3):
#     seen = set()
#     result = []
#     for item in list1 + list2 + list3:
#         if item not in seen:        # set lookup is faster than list lookup
#             seen.add(item)
#             result.append(item)
#     return result
#
# print(get_unique(list1, list2, list3))

# ###########     Way 4 — Using *args (accept ANY number of lists)
# def get_unique(*lists):             # *args accepts any number of lists
#     combined = []
#     for lst in lists:               # loop each list
#         combined += lst             # merge one by one
#     return list(set(combined))
#
# # works with 2, 3, 4, or more lists!
# print(get_unique(list1, list2))
# print(get_unique(list1, list2, list3))
# print(get_unique(list1, list2, list3, [10, 11, 1]))

# ##############      Way 5 — Using set union operator (most elegant)
# def get_unique(*lists):
#     result = set()                      # start with empty set
#     for lst in lists:
#         result = result | set(lst)      # | = union → merges & removes duplicates
#     return list(result)
#
# # OR even shorter using reduce:
# from functools import reduce
#
# def get_unique_short(*lists):
#     return list(reduce(lambda a, b: set(a) | set(b), lists))
#
# print(get_unique(list1, list2, list3))
# print(get_unique_short(list1, list2, list3))

# ########### Way 6 — Bonus: find elements unique to ONLY ONE list (not shared)
# def truly_unique(*lists):
#     from collections import Counter
#     combined = []
#     for lst in lists:
#         combined += lst
#
#     count = Counter(combined)
#     return [item for item in combined if count[item] == 1]
#
# print(truly_unique(list1, list2, list3))