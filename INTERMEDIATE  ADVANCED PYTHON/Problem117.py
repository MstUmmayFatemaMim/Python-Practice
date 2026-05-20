# ##########   117. Unintended Mutation Through Return Value
# Write a function that:
# Returns a list
# Caller modifies it
# Original internal data gets corrupted
#  Fix the design so original one do not get affected
# def get_data():
#     return internal
# internal = []
# x = get_data()
# x.append(1)
#

def get_data():
    return internal.copy()      ####### create copy --> new memory
internal = [1,2,3,4]
x = get_data()
x.append(1)
print(x)
print(internal)
print(id(internal)==id(x))