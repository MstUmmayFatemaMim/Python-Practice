############    Find the common elements between two lists.

# list1=[1,2,3,4,5,6,7,8,9]
# list2=[11,22,33,44,5,6,7,8,9]
# list3=[]
# for x in list1:
#     for y in list2:
#         if x==y:
#             list3.append(x)
# print(list3)

############    Use Set
set1={1,2,3,4,5,6,7,8,9}
set2={11,22,33,44,5,6,7,8,9}
set3=set()         ####### create empty set.
for x in set1:
    for y in set2:
        if x==y:
            set3.add(x)
print(set3)

# # # Find common items using the & operator
# # common_items = set1 & set2
# # print(common_items)
# common_items = set1.intersection(set2)
# print(common_items)
#
# common_items = {x for x in set1 if x in set2}
# print(common_items)
# ############     list Comprehension
# common_items = [x for x in set1 if x in set2]
# print(common_items)
#
# common_items = set(filter(lambda x: x in set2, set1))
# print(common_items)
