# ########        114. In-Place vs Rebinding/Reassigning
# Write two functions:
# One modifies a list in place
# One rebinds the list
#  Prove the difference using function calls.


def inplace(lst):
    lst.append(99)
    return lst
print("Inplace List : ")
original_list=[1,3,4,6]
newlist=inplace(original_list)
print(newlist)
print(original_list)
print(id(original_list)==id(newlist))

def rebind(lst):
    lst=lst+[89]
    return lst
print("Rebind List : ")
original_list=[1,3,4,6]
newlist=rebind(original_list)
print(newlist)
print(original_list)
print(id(original_list)==id(newlist))





