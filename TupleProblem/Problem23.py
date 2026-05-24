# ###########     Count how many times an element appears in a tuple.
#
# # tuple1=(1,2,5,4,5,1,7,2,9) #touple e value assign
# mytuple = (50, 30, 70, 30, 500, 30, 60)
#
# for x in mytuple:      #take every value
#     count = 0
#     for y in mytuple:    # take full touple
#         if y == x:
#             count = count + 1
#     print(f"{x} have {count} times")


# #########   Prove the code
# # mytuple = (50, 30, 70, 30, 500, 30, 60)
# #
# # # your way — count the steps
# # steps = 0
# # for x in mytuple:
# #     count = 0
# #     for y in mytuple:
# #         steps += 1         # count every check
# #         if y == x:
# #             count += 1
# # print("Your way steps:", steps)
# #
# # # boss way — count the steps
# # steps = 0
# # for i in range(len(mytuple)):
# #     x = mytuple[i]
# #     count = 1
# #     for j in range(len(mytuple)):
# #         if j != i:
# #             steps += 1     # count every check
# #             if mytuple[j] == x:
# #                 count += 1
# # print("Boss way steps:", steps)
#
#
# mytuple = (50, 30, 70, 30, 500, 30, 60)
#
# # # ─────────────────────────────────────────
# # # Fix 1 — skip already counted elements
# # # avoid printing same element multiple times
# # # ─────────────────────────────────────────
# # checked = ()               # track already counted elements
# #
# # for x in mytuple:
# #     if x not in checked:   # only count each element once
# #         count = 0
# #         for y in mytuple:
# #             if y == x:
# #                 count += 1
# #         print(f"{x} appears {count} times")
# #         checked = checked + (x,)   # mark as counted
# #
# #
# # # # ─────────────────────────────────────────
# # # # Fix 2 — your boss's way
# # # # start count from 1 — x already exists
# # # # inner loop skips x's own position using index
# # # # ─────────────────────────────────────────
# checked = ()
#
# for i in range(len(mytuple)):
#     x = mytuple[i]
#     if x not in checked:
#         count = 1                        # x exists → start from 1
#         for j in range(i+1,len(mytuple)):
#             if j != i and mytuple[j] == x:  # skip x's own position
#                 count += 1
#         print(f"{x} appears {count} times")
#         checked = checked + (x,)
#
# mytuple = (50, 30, 70, 30, 500, 30, 60)
# checked = ()
#
# for x in mytuple:
#     if x not in checked:
#         print(f"{x} appears {mytuple.count(x)} times")
#         checked = checked + (x,)

# ############    Use Dictionary
from collections import Counter
mytuple = (50, 30, 70, 30, 500, 30, 60)
counts = Counter(mytuple)
print(counts)

# mytuple = (50, 30, 70, 30, 500, 30, 60)
# counts = {}
#
# for item in mytuple:
#     counts[item] = counts.get(item, 0) + 1
#
# print(counts)
