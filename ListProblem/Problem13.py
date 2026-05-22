##############      Insert an element at index 0 without using insert().
newlist = [50, 30, 70, 190, 500, 200, 60]
newlist = [10] + newlist
print(newlist)

# newlist = [50, 30, 70, 190, 500, 200, 60]
#
# # ─────────────────────────────────────────
# # Way 1 — Your way (list concatenation)
# # just add new element as list before original
# # ─────────────────────────────────────────
# newlist = [10] + newlist
# print("Way 1:", newlist)
#
#
# # ─────────────────────────────────────────
# # Way 2 — slicing
# # [:0] means "before index 0" = very beginning
# # ─────────────────────────────────────────
# newlist = [50, 30, 70, 190, 500, 200, 60]
# newlist[0:0] = [10]        # insert at position 0 using slice
# print("Way 2:", newlist)
#
#
# # ─────────────────────────────────────────
# # Way 3 — loop shift (most manual way)
# # shift every element one step right
# # then place new element at index 0
# # ─────────────────────────────────────────
# newlist = [50, 30, 70, 190, 500, 200, 60]
# newlist.append(None)       # add empty space at end first
#
# for i in range(len(newlist)-1, 0, -1):  # loop backwards
#     newlist[i] = newlist[i-1]           # shift each item right
#
# newlist[0] = 10            # now place new element at front
# print("Way 3:", newlist)
#
#
# # ─────────────────────────────────────────
# # Way 4 — list unpacking (*)
# # * unpacks all elements of original list
# # ─────────────────────────────────────────
# newlist = [50, 30, 70, 190, 500, 200, 60]
# newlist = [10, *newlist]   # unpack original after 10
# print("Way 4:", newlist)
#
#
# # ─────────────────────────────────────────
# # Way 5 — deque (double ended queue)
# # appendleft() adds to front — O(1) fastest way
# # ─────────────────────────────────────────
# from collections import deque
# newlist = [50, 30, 70, 190, 500, 200, 60]
# dq = deque(newlist)        # convert list to deque
# dq.appendleft(10)          # add 10 at front
# newlist = list(dq)         # convert back to list
# print("Way 5:", newlist)
#
#
# # ─────────────────────────────────────────
# # Way 6 — list comprehension + enumerate
# # build new list with 10 at front
# # ─────────────────────────────────────────
# newlist = [50, 30, 70, 190, 500, 200, 60]
# newlist = [10] + [newlist[i] for i in range(len(newlist))]
# print("Way 6:", newlist)
#
#
# # ─────────────────────────────────────────
# # Way 7 — using * unpacking in function
# # ─────────────────────────────────────────
# newlist = [50, 30, 70, 190, 500, 200, 60]
#
# def insert_at_front(element, lst):
#     return [element] + lst       # same as Way 1 but reusable
#
# newlist = insert_at_front(10, newlist)
# print("Way 7:", newlist)
