                #######Flatten a list like: [[1,2],[3,4]] → [1,2,3,4]

# age=[[4,7,9,3], [34,55,63,88]]
# proage=[]
# for x in age:
#     proage.extend(x)
# print(proage)

age = [[1,2],[3,4]]
proage = [item for x in age for item in x]       # Read it like two nested for loops:
# for x in age:        # x = [1,2], then [3,4]
#     for item in x:   # item = 1,2, then 3,4
#         collect item
print(proage)

# import itertools
# age = [[1,2],[3,4],[5,6],[7,8]]
# proage = list(itertools.chain.from_iterable(age))
# # chain.from_iterable([[1,2],[3,4]])
# #        ↓
# # chains them → 1, 2, 3, 4  (like a stream)
# #          ↓
# # list() collects the stream → [1, 2, 3, 4]
# print(proage)

# age = [[1,2],[3,4]]
# proage = sum(age, [])
# print(proage)

# from functools import reduce
# age = [[1,2],[3,4],[5,6]]
# proage = reduce(lambda acc, x: acc + x, age) # reduce applies the lambda left to right:Step 1: acc=[1,2], x=[3,4]  →  [1,2] + [3,4] = [1,2,3,4]
# acc  →  result so far (accumulator)
#     x    →  next item in the list
# print(proage)

# age = [[1,2],[3,4],[5,6]]
# proage = []
# for x in age:
#     for item in x:
#         proage.append(item)
# print(proage)

# import numpy as np  #use numpy and need to install it
# age = [[1,2],[3,4]]
# proage = np.array(age).flatten().tolist()
# # np.array([[1,2],[3,4]])  →  2D array
# # .flatten()               →  1D array [1,2,3,4]
# # .tolist()                →  Python list [1,2,3,4]
# print(proage)

# age = [[1,2],[3,4],[5,6]]
# proage = []
# [proage.extend(x) for x in age]
# print(proage)
