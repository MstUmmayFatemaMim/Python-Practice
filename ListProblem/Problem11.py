# ########### Remove all negative numbers from a list.
#
newlist = [50, -30, 70, 190, -500, 0, 200]

newlist = [i for i in newlist if i >= 0]
print(newlist)
#
#
# # ─────────────────────────────────────────
# # Way 2 — Basic for loop + append
# # most beginner friendly
# # ─────────────────────────────────────────
# result = []
# for i in newlist:
#     if i >= 0:
#         result.append(i)   # only keep positive and zero
# print("Way 2:", result)
#
#
# # ─────────────────────────────────────────
# # Way 3 — filter() built-in
# # filter(function, list) — keeps items where function = True
# # ─────────────────────────────────────────
# result = list(filter(lambda x: x >= 0, newlist))
# print("Way 3:", result)
#
#
# # ─────────────────────────────────────────
# # Way 4 — while loop
# # ─────────────────────────────────────────
# result = []
# i = 0
# while i < len(newlist):
#     if newlist[i] >= 0:
#         result.append(newlist[i])
#     i += 1
# print("Way 4:", result)
#
#
# # ─────────────────────────────────────────
# # Way 5 — remove negatives from original list
# # careful — never modify a list while looping it directly!
# # always loop a COPY, modify the original
# # ─────────────────────────────────────────
# temp = newlist.copy()         # loop the copy
# for i in temp:
#     if i < 0:
#         newlist.remove(i)     # remove from original
# print("Way 5:", newlist)
#
#
# # ─────────────────────────────────────────
# # Way 6 — using enumerate (index + value)
# # ─────────────────────────────────────────
# result = []
# for index, value in enumerate(newlist):
#     if value >= 0:
#         result.append(value)
# print("Way 6:", result)
#
#
# # # ─────────────────────────────────────────
# # # Way 7 — numpy (for large data)
# # # pip install numpy
# # # ─────────────────────────────────────────
# # import numpy as np
# # arr    = np.array(newlist)
# # result = arr[arr >= 0]        # numpy filters in one step
# # print("Way 7:", result)