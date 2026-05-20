# #######     118. Time Complexity Awareness
# Write two versions of code that:
# Insert 1000 items at index 0 in a list
# Append 1000 items at the end
#  Measure (roughly) which one is slower and explain why

# original_list = [10, 20, 30]        ## O(n)
# new_items = list(range(1000))        ## O(m)
# print(new_items+original_list)       ## O(n+m))
# original_list.extend(new_items)          ## O(n)
# print(original_list)                 ## O(n)


# import timeit
# from collections import deque
#
# n = 1000
#
# t1 = timeit.timeit(
#     stmt="for i in range(n): lst.insert(0, i)",
#     setup="lst = []; n = 1000",
#     number=100
# )
#
# t2 = timeit.timeit(
#     stmt="for i in range(n): lst.append(i)",
#     setup="lst = []; n = 1000",
#     number=100
# )
#
# print(f"insert(0): {t1:.4f}s")
# print(f"append:    {t2:.4f}s")

# import time
#
# # ── Version 1: insert at index 0 (slow) ──
# lst1 = []
# start = time.time()
#
# for i in range(100):
#     lst1.insert(0, i)
#
# end = time.time()
# insert_time = end - start
#
# # ── Version 2: append at end (fast) ──
# lst2 = []
# start = time.time()
#
# for i in range(100):
#     lst2.append(i)
#
# end = time.time()
# append_time = end - start
#
# # ── Results ──
# print(f"insert(0) time : {insert_time:.6f} seconds")
# print(f"append    time : {append_time:.6f} seconds")
# print(f"insert is {insert_time / append_time:.1f}x slower than append")

# lst1 = []
# for i in range(100):
#     lst1.insert(0, i)
# print(lst1)
#
# lst2 = []
# for i in range(100):
#     lst2.append(i)
# print(lst2)

# ── Version 1: insert at index 0 ──
lst1 = []
ops1 = 0          # our manual counter

for i in range(100):
    lst1.insert(0, i)
    ops1 += len(lst1)   # each insert shifts ALL current elements
                        # so cost = current size of list

print("List:", lst1)
print(f"Total operations (insert): {ops1}")


# ── Version 2: append ──
lst2 = []
ops2 = 0          # our manual counter

for i in range(100):
    lst2.append(i)
    ops2 += 1     # append always costs exactly 1 — no shifting

print("List:", lst2)
print(f"Total operations (append): {ops2}")


# ── Compare ──
print(f"\ninsert used {ops1} operations")
print(f"append used {ops2} operations")
print(f"insert did {ops1 // ops2}x more work than append")