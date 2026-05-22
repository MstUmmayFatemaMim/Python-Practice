# ###########     Replace all even numbers with 0.
testlist=[1,4,6,8,9,10,33,24,50,55,76,69]
newlist=[]
print(len(testlist))
i=0
while i<len(testlist):
        if testlist[i]%2==0:        #### use i means index devided by 2.testlist[i] means value divided by 2
            newlist.append(0)
        else:
            newlist.append(testlist[i])
        i=i+1
print(newlist)
#
#
# # ─────────────────────────────────────────
# # Way 2 — for loop + append
# # cleaner than while — no need to manage i manually
# # ─────────────────────────────────────────
# newlist = []
# for x in testlist:
#     if x % 2 == 0:              # even → replace with 0
#         newlist.append(0)
#     else:
#         newlist.append(x)       # odd → keep original
# print("Way 2:", newlist)
#
#
# # ─────────────────────────────────────────
# # Way 3 — list comprehension (one line)
# # most Pythonic and shortest way
# # ─────────────────────────────────────────
# newlist = [0 if x % 2 == 0 else x for x in testlist]
# #           ↑ even → 0      ↑ odd → keep x
# print("Way 3:", newlist)
#
#
# # ─────────────────────────────────────────
# # Way 4 — modify original list directly
# # using enumerate to get index + value
# # ─────────────────────────────────────────
# testlist2 = testlist.copy()         # protect original
# for index, value in enumerate(testlist2):
#     if value % 2 == 0:              # even → replace with 0
#         testlist2[index] = 0        # change at that index directly
# print("Way 4:", testlist2)
#
#
# # ─────────────────────────────────────────
# # Way 5 — using map() built-in
# # map applies a function to every element
# # ─────────────────────────────────────────
# def replace_even(x):
#     return 0 if x % 2 == 0 else x  # even → 0, odd → keep
#
# newlist = list(map(replace_even, testlist))
# print("Way 5:", newlist)
#
#
# # ─────────────────────────────────────────
# # Way 6 — map() with lambda (one line)
# # same as Way 5 but without defining a function
# # ─────────────────────────────────────────
# newlist = list(map(lambda x: 0 if x % 2 == 0 else x, testlist))
# #                  ↑ lambda = small one line function
# print("Way 6:", newlist)
#
#
# # ─────────────────────────────────────────
# # Way 7 — numpy (best for large datasets)
# # pip install numpy
# # ─────────────────────────────────────────
# import numpy as np
# arr = np.array(testlist)
# arr[arr % 2 == 0] = 0      # replace all even positions with 0
# print("Way 7:", arr)