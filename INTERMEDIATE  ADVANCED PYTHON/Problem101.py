# # #############   101. Shallow vs Deep Copy (Nested)
# # Write a function safe_copy(data) that:
# # Accepts a dictionary containing lists as values
# #
# #
# # Returns a fully independent copy
# #
# #
# # Modifying any nested list in the copy must NOT affect the original
# #
# #
# # Test Case
# # data = {"a": [1, 2], "b": [3, 4]}
# # new_data = safe_copy(data)
# # new_data["a"].append(99)
#
#
def safe_copy(data):
    new = {}
    for key, value in data.items():     # O(n*m)
        new[key] = value[:]             # [:] creates new list copy
    return new

# ---- Test ----
data     = {"a": [1, 2], "b": [3, 4]}
new_data = safe_copy(data)

new_data["a"].append(99)

print("Original:", data)
print("Copy:    ", new_data)


# #########   Solution 1 — Using deepcopy (simplest)
# import copy
#
# def safe_copy(data):
#     return copy.deepcopy(data)      # O(n*m) n=keys, m=list length
#
# # ---- Test ----
# data     = {"a": [1, 2], "b": [3, 4]}
# new_data = safe_copy(data)
#
# new_data["a"].append(99)
#
# print("Original:", data)
# print("Copy:    ", new_data)
# print("Same?", data is new_data)
# print("Inner same?", data["a"] is new_data["a"])

# ############    Solution 3 — Dictionary comprehension (most compact)
# def safe_copy(data):
#     return {key: list(value)            # list() creates new copy
#             for key, value in data.items()}   # O(n*m)
#
# # ---- Test ----
# data     = {"a": [1, 2], "b": [3, 4]}
# new_data = safe_copy(data)
#
# new_data["b"].append(99)
#
# print("Original:", data)
# print("Copy:    ", new_data)