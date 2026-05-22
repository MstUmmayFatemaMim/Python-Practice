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