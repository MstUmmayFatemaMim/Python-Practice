################    Group numbers into even and odd using dictionary.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = {"even": [], "odd": []}
for n in numbers:
    if n % 2 == 0:
        result["even"].append(n)
    else:
        result["odd"].append(n)

print(result)


# # Way 2 — Dictionary comprehension (compact)
# result = {
#     "even": [n for n in numbers if n % 2 == 0],
#     "odd":  [n for n in numbers if n % 2 != 0]
# }
#
# print(result)

##########Way 3 — Using a key label trick (clever one-loop)
# result = {"even": [], "odd": []}
#
# for n in numbers:
#     key = "even" if n % 2 == 0 else "odd"   # decide the key first
#     result[key].append(n)                    # then append directly
#
# print(result)

##########  Way 4 — Using setdefault() (dynamic keys)
# result = {}
#
# for n in numbers:
#     key = "even" if n % 2 == 0 else "odd"
#     result.setdefault(key, []).append(n)    # creates key if it doesn't exist
#
# print(result)

# ############    Way 5 — Using groupby from itertools (advanced)
# from itertools import groupby
#
# numbers_sorted = sorted(numbers, key=lambda n: n % 2)  # evens first
# result = {}
#
# for key, group in groupby(numbers_sorted, key=lambda n: n % 2):
#     result["even" if key == 0 else "odd"] = list(group)
#
# print(result)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# grouped_dict = {}
#
# for num in numbers:
#     # Determine the category based on the modulo operator
#     category = "even" if num % 2 == 0 else "odd"
#
#     # Append to the correct list in the dictionary
#     grouped_dict.setdefault(category, []).append(num)
#
# print(grouped_dict)
