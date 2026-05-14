############Write a function that modifies a list in place.

def mfunction(oldlist,newlist):
    newlist = oldlist.copy()
    # newlist[1]=99
    newlist.append(99)
    return newlist

o=[2,4,5,6]
p=mfunction(o,[])
print(o)
print(p)

# old_list=[2,4,5,6]
# new_list=old_list.copy()
# print(old_list)
# print(new_list)
# new_list[1]=99
# print(new_list)
# print(old_list)