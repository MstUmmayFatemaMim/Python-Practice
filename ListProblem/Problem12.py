# ##########    Find the second largest number in a list.
# ###### Loop শেষ হওয়ার পর i এর value = 5 (last index)
# ##### সেটা second largest এর index না
# ##### এটা শুধু coincidence যে 200 correct ছিল
# # # newlist4=[50,30,70,190,500,200]
# # # listmax = newlist4[0]
# # # for i in range(len(newlist4)):
# # #     if newlist4[i]>=listmax:
# # #         listmax=newlist4[i]
# # # if newlist4[i]<=listmax:
# # #     print(newlist4[i])
# #
# newlist4 = [50, 30, 70, 190, 500, 200]
#
# # Start both tracking variables with the first item
# largest = newlist4[0]
# second_largest = 0  # Start with negative infinity as a safe baseline
#
# for i in range(len(newlist4)):
#     current_num = newlist4[i]
#
#     # 1. If current number is bigger than the largest, shift the titles
#     if current_num > largest:
#         second_largest = largest  # The old largest becomes second largest
#         largest = current_num  # The current number becomes the new largest
#
#     # 2. If it's not bigger than largest, but bigger than second largest
#     elif current_num > second_largest and current_num != largest:
#         second_largest = current_num
#
# print("The second largest number is:", second_largest)
# # # Output: 200
#
# # newlist4 = [50, 30, 70, 190, 500, 200]
# #
# # # Remove duplicates using set(), sort them, and pick the second item from the end
# # unique_sorted = sorted(list(set(newlist4)))
# # second_largest = unique_sorted[-2]
# #
# # print(second_largest)
# #
# newlist = [50, 30, 70, 190, 500, 200]
# #
# # # ─────────────────────────────────────────
# # # Way 1 — Two loop approach (most beginner friendly)
# # # Step 1: find max, Step 2: find second largest
# # # ─────────────────────────────────────────
# # # Step 1
# # listmax = newlist[0]
# # for i in range(len(newlist)):
# #     if newlist[i] > listmax:
# #         listmax = newlist[i]
# #
# # # Step 2
# # second = None
# # for i in range(len(newlist)):
# #     if newlist[i] != listmax:          # skip the maximum
# #         if second is None or newlist[i] > second:
# #             second = newlist[i]        # update second largest
# #
# # print("Way 1:", second)                # 200
# #
# #
# # # ─────────────────────────────────────────
# # # Way 2 — One loop, two variables
# # # track max and second at same time
# # # ─────────────────────────────────────────
# # listmax = None
# # second  = None
# #
# # for i in newlist:
# #     if listmax is None or i > listmax:
# #         second  = listmax   # old max becomes second
# #         listmax = i         # new max found
# #     elif second is None or (i > second and i != listmax):
# #         second = i          # update second if bigger
# #
# # print("Way 2:", second)     # 200
# #
# #
# # # ─────────────────────────────────────────
# # # Way 4 — using set() to remove duplicates first
# # # handles duplicate values safely
# # # example: [500, 500, 200] → set → {200, 500}
# # # ─────────────────────────────────────────
# # unique_list = list(set(newlist))       # remove duplicates
# # unique_list.sort()                     # sort ascending
# # print("Way 4:", unique_list[-2])       # second from end = 200
#
#
# # # ─────────────────────────────────────────
# # # Way 5 — remove max then find max again
# # # simple logic — remove biggest, biggest remaining = second
# # # ─────────────────────────────────────────
# # temp = newlist.copy()                  # protect original list
# newlist.remove(max(newlist))                 # remove the largest
# print("Way 5:", max(newlist))             # now max = second largest
#
#
# # # ─────────────────────────────────────────
# # # Way 6 — using sorted() + set() one line
# # # cleanest one line solution
# # # ─────────────────────────────────────────
# # print("Way 6:", sorted(set(newlist))[-2])
#
#
# # # ─────────────────────────────────────────
# # # Way 7 — numpy (for large datasets)
# # # pip install numpy
# # # ─────────────────────────────────────────
# # import numpy as np
# # arr    = np.array(newlist)
# # unique = np.unique(arr)                # removes duplicates + sorts
# # print("Way 7:", unique[-2])            # second from end = 200
#

newlist=[3,5,2,9,30,45,4]
# newlist.remove(max(newlist))                 # remove the largest
# print(max(newlist))

updatelist=sorted(newlist)
print(updatelist[-2])

newlist.sort()
print(newlist[-2])
