# # ###########     Split a list into two halves.
# newlist = [50, 30, 70, 190, 500, 200,60]
# x = len(newlist)//2
# print(newlist[x:])
# print(newlist[:x])
#
# newlist = [50, 30, 70, 190, 500, 200, 60]
#
#
# # # ─────────────────────────────────────────
# # # Way 2 — Manual loop (most basic)
# # # ─────────────────────────────────────────
# first_half  = []
# second_half = []
# mid = len(newlist) // 2
#
# for i in range(len(newlist)):
#     if i < mid:
#         first_half.append(newlist[i])
#     else:
#         second_half.append(newlist[i])
# print(f"First Half : {first_half}   Second Half {second_half}")


# # ─────────────────────────────────────────
# # Way 3 — Using unpacking (*)
# # ─────────────────────────────────────────
# mid = len(newlist) // 2
# first_half, second_half = newlist[:mid], newlist[mid:]
# print("Way 3:", first_half, "|", second_half)
#
#
# # ─────────────────────────────────────────
# # Way 4 — Using a function
# # ─────────────────────────────────────────
# def split_list(lst):
#     mid = len(lst) // 2
#     return lst[:mid], lst[mid:]   # returns two halves
#
# first_half, second_half = split_list(newlist)
# print("Way 4:", first_half, "|", second_half)
#
#
# # ─────────────────────────────────────────
# # Way 5 — Using list comprehension with index
# # ─────────────────────────────────────────
# mid = len(newlist) // 2
# first_half  = [newlist[i] for i in range(mid)]
# second_half = [newlist[i] for i in range(mid, len(newlist))]
# print("Way 5:", first_half, "|", second_half)


# # ─────────────────────────────────────────
# # Way 1 — Using numpy (scientific library)
# # pip install numpy
# # ─────────────────────────────────────────
# import numpy as np
#
# halves = np.array_split(newlist, 2)  # splits into 2 equal parts
# print("Way 1:", halves[0], "|", halves[1])
#
#
# # ─────────────────────────────────────────
# # Way 2 — Using itertools (built-in)
# # ─────────────────────────────────────────
# from itertools import islice
#
# def split_itertools(lst, n):
#     it = iter(lst)                        # convert list to iterator
#     first_half  = list(islice(it, n))     # take first n items
#     second_half = list(islice(it, None))  # take remaining items
#     return first_half, second_half
#
# mid = len(newlist) // 2
# first_half, second_half = split_itertools(newlist, mid)
# print("Way 2:", first_half, "|", second_half)
#
#
# # ─────────────────────────────────────────
# # Way 3 — Using zip (built-in)
# # ─────────────────────────────────────────
# mid = len(newlist) // 2
# first_half  = list(newlist[:mid])
# second_half = list(newlist[mid:])
# paired = list(zip(first_half, second_half))  # pairs items together
# print("Way 3 paired:", paired)
# # [(50,190), (30,500), (70,200)]  ← each pair = one from each half
#
#
# # ─────────────────────────────────────────
# # Way 4 — Using map + slice (built-in)
# # ─────────────────────────────────────────
# mid = len(newlist) // 2
# first_half, second_half = map(list, [newlist[:mid], newlist[mid:]])
# print("Way 4:", first_half, "|", second_half)
#
#
# # ─────────────────────────────────────────
# # Way 5 — numpy split into 3 parts
# # ─────────────────────────────────────────
# import numpy as np
#
# parts = np.array_split(newlist, 3)   # splits into 3 parts
# print("Way 5:", parts[0], parts[1], parts[2])
