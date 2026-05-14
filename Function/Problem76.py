#####Write a function that returns a new list without modifying original.

def mfunction(oldlist,newlist):
    newlist = oldlist.copy()
    newlist.extend([4, 5, 6])
    return newlist

o=[2,4,5,6]
p=mfunction(o,[])
print(p)
print(o)


# old_list=[2,4,5,6]
# new_list=old_list.copy()
# print(old_list)
# print(new_list)
# new_list.extend([4,5,6])
# print(new_list)
# print(old_list)