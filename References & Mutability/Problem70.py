# ######Fix the function to avoid modification.
# ########Method 1 — isinstance() Check (Manual Approach)
def duplicate2dList(oldList):
    result = []
    for l in oldList:
        if isinstance(l, list):
            result.append(list(l))  # inner list → copy it
        else:
            result.append(l)        # primitive → just append
    return result

# 1D
slist1 = [3, 7, 5, 8, 33, 56]
copy1 = duplicate2dList(slist1)
copy1[4] = 999
print(slist1)  # [3, 7, 5, 8, 33, 56]  ✅ unchanged
print(copy1)   # [3, 7, 5, 8, 999, 56]

# 2D
slist2 = [[3, 5], [6, 33], [6, 7]]
copy2 = duplicate2dList(slist2)
copy2[0][0] = 999
print(slist2)  # [[3, 5], [6, 33], [6, 7]]  ✅ unchanged
print(copy2)   # [[999, 5], [6, 33], [6, 7]]
        ## How it works:
       # # Checks each element with isinstance(l, list) to decide how to copy it
       # # If element is a list → copy it with list(l)
       # # If element is a primitive (int, str) → append directly
       # # Simple and very readable but only handles exactly 1D or 2D, not deeper
# #
# #
# # Method 2 — List Comprehension with isinstance() (Pythonic)
# def duplicate2dList(oldList):
#     return [list(l) if isinstance(l, list) else l for l in oldList]
#
# # 1D
# slist1 = [3, 7, 5, 8, 33, 56]
# copy1 = duplicate2dList(slist1)
# copy1[4] = 999
# print(slist1)  # [3, 7, 5, 8, 33, 56]  ✅ unchanged
# print(copy1)   # [3, 7, 5, 8, 999, 56]
#
# # 2D
# slist2 = [[3, 5], [6, 33], [6, 7]]
# copy2 = duplicate2dList(slist2)
# copy2[0][0] = 999
# print(slist2)  # [[3, 5], [6, 33], [6, 7]]  ✅ unchanged
# print(copy2)   # [[999, 5], [6, 33], [6, 7]]
        # # How it works:
        # # Same logic as Method 1 but written in a single line
        # # Uses ternary expression inside list comprehension
        # # More Pythonic and concise


# # Method 3 — copy.deepcopy() ✅ Best & Safest
# import copy
#
# def duplicate2dList(oldList):
#     return copy.deepcopy(oldList)
#
# # 1D
# slist1 = [3, 7, 5, 8, 33, 56]
# copy1 = duplicate2dList(slist1)
# copy1[4] = 999
# print(slist1)  # [3, 7, 5, 8, 33, 56]  ✅ unchanged
# print(copy1)   # [3, 7, 5, 8, 999, 56]
#
# # 2D
# slist2 = [[3, 5], [6, 33], [6, 7]]
# copy2 = duplicate2dList(slist2)
# copy2[0][0] = 999
# print(slist2)  # [[3, 5], [6, 33], [6, 7]]  ✅ unchanged
# print(copy2)   # [[999, 5], [6, 33], [6, 7]]
#
        # # How it works:
        # # deepcopy() recursively copies every element at any depth
        # # Works for 1D, 2D, 3D or any nested structure automatically
        # # No manual checks needed — handles everything in one call
        # # Best choice when the input structure is unknown or complex
#
#
# #Method 4 — Recursive Function (Custom Deep Copy)
# def duplicate2dList(oldList):
#     result = []
#     for l in oldList:
#         if isinstance(l, list):
#             result.append(duplicate2dList(l))  # recurse into inner list
#         else:
#             result.append(l)
#     return result
#
# # 1D
# slist1 = [3, 7, 5, 8, 33, 56]
# copy1 = duplicate2dList(slist1)
# copy1[4] = 999
# print(slist1)  # [3, 7, 5, 8, 33, 56]  ✅ unchanged
# print(copy1)   # [3, 7, 5, 8, 999, 56]
#
# # 2D
# slist2 = [[3, 5], [6, 33], [6, 7]]
# copy2 = duplicate2dList(slist2)
# copy2[0][0] = 999
# print(slist2)  # [[3, 5], [6, 33], [6, 7]]  ✅ unchanged
# print(copy2)   # [[999, 5], [6, 33], [6, 7]]
#
# # Bonus — 3D also works ✅
# slist3 = [[[1, 2], [3, 4]], [[5, 6]]]
# copy3 = duplicate2dList(slist3)
# copy3[0][0][0] = 999
# print(slist3)  # [[[1, 2], [3, 4]], [[5, 6]]]  ✅ unchanged
# print(copy3)   # [[[999, 2], [3, 4]], [[5, 6]]]
# # How it works:
# #
# # The function calls itself when it finds an inner list
# # Digs into any level of nesting automatically
# # Great for learning recursion — builds the same logic as deepcopy() from scratch
# # No imports needed
#
#
# Method 5 — json Serialize/Deserialize
import json
def duplicate2dList(oldList):
    return json.loads(json.dumps(oldList))
# 1D
# slist1 = [3, 7, 5, 8, 33, 56]
# copy1 = duplicate2dList(slist1)
# copy1[4] = 999
# print(slist1)  # [3, 7, 5, 8, 33, 56]  ✅ unchanged
# print(copy1)   # [3, 7, 5, 8, 999, 56]
# # 2D
# slist2 = [[3, 5], [6, 33], [6, 7]]
# copy2 = duplicate2dList(slist2)
# copy2[0][0] = 999
# print(slist2)  # [[3, 5], [6, 33], [6, 7]]  ✅ unchanged
# print(copy2)   # [[999, 5], [6, 33], [6, 7]]
# # How it works:
# # json.dumps() converts the list to a JSON string
# # json.loads() parses it back into a brand new list
# # Since it's rebuilt from a string, it's fully independent
# # ❌ Only works with JSON-safe types (int, float, str, list, dict) — fails on objects, sets, tuples
# #
#
# # Method 6 — map() with isinstance() Check
# def duplicate2dList(oldList):
#     return list(map(lambda l: list(l) if isinstance(l, list) else l, oldList))
# # 1D
# slist1 = [3, 7, 5, 8, 33, 56]
# copy1 = duplicate2dList(slist1)
# copy1[4] = 999
# print(slist1)  # [3, 7, 5, 8, 33, 56]  ✅ unchanged
# print(copy1)   # [3, 7, 5, 8, 999, 56]
#
# # 2D
# slist2 = [[3, 5], [6, 33], [6, 7]]
# copy2 = duplicate2dList(slist2)
# copy2[0][0] = 999
# print(slist2)  # [[3, 5], [6, 33], [6, 7]]  ✅ unchanged
# print(copy2)   # [[999, 5], [6, 33], [6, 7]]
# # How it works:
# # map() applies a lambda function to every element
# # Lambda checks isinstance — copies inner lists, passes primitives through
# #Functional programming style — useful to know but less readable than comprehension