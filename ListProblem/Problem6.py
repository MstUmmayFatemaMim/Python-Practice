# ######### Count how many times a value appears in a list.
# newlist5 = [50, 30, 70, 190, 500, 200, 50, 30]
# seen=[]
# for x in newlist5:
#     if x not in seen:
#         count=0
#         for y in newlist5:
#             if x == y:
#                 count+=1
#         print(f"The count of {x} is {count}")
#         seen.append(x)


# ###########     Dictionary
# # newlist={50, 30, 70, 190, 500, 200, 50, 30}       ######## without key this curly bracket automatically convert into set.Set also
# #                                                   ############## automatically remove the duplicate value and we can not get exact value
# newlist=[50, 30, 70, 190, 500, 200, 50, 30]
#
# count={}
# for x in newlist:
#     if x in count:
#         count[x]+=1
#     else:
#         count[x]=1
# print(count)

# # #############     Touple
# newlist = (50, 30, 70, 190, 500, 200, 50, 30,200)
# checked = ()   # track what we already counted
# for x in newlist:
#     if x not in checked:
#         print(f"{x} appears {newlist.count(x)} times")
#         checked = checked + (x,)


# # why (x,) and not just (x)?
# a = (50)    # what is this? ---> This is int type
# b = (50,)   # what is this? ---> This is tuple
# print(type(a))
# print(type(b))

# ##########   Build in function
# from collections import Counter
#
# newlist = [50, 30, 70, 190, 500, 200, 50, 30]
#
# # Pass the collection directly into Counter
# count = Counter(newlist)
#
# # print(count)
# # Output: Counter({50: 2, 30: 2, 70: 1, 190: 1, 500: 1, 200: 1})


# ###########   Build in function
# from collections import Counter
# newlist = [50, 30, 70, 190, 500, 200, 50, 30]
#
# # Pass the collection directly into Counter
# count = Counter(newlist)
# # Convert to a standard dictionary
# standard_dict = dict(count)  # Output: {50: 2, 30: 2, ...}
# print(standard_dict)
# # Convert to a list of pairs
# pairs_list = list(count.items())  # Output: [(50, 2), (30, 2), ...]
# print(pairs_list)
