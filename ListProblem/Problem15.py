#################   Rotate a list left by one position.

# newlist= [50, 30, 70, 190, 500, 200,60]
#
# result = newlist[1:] + [newlist[0]]
# print("LEFT :", result)
#
# # result = [newlist[-1]] + newlist[:-1]
# # print("Right :", result)

mylist = [1, 2, 3, 4, 5]
rotated = mylist[1:] + mylist[:1]
print(rotated)

# from collections import deque
#
# mylist = [1, 2, 3, 4, 5]
#
# # Convert to deque, rotate left by 1, and convert back to list
# d = deque(mylist)
# d.rotate(-1)
# rotated = list(d)
#
# print(rotated)
