# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
#
# thisset.update(tropical)
#
# print(thisset)
# thisset = {"apple", "banana", "cherry"}
#
# thisset.remove("banana")
#
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
#
# x = thisset.pop()
#
# print(x) #removed item
#
# print(thisset) #the set after removal

# thisset = {"apple", "banana", "cherry"}
#
# # thisset.clear()
#
# print(type(thisset))
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)