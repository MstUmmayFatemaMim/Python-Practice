########    Remove an element safely from a set.
myset = {2,3,5,7,8,1,9}
myset.remove(1)
print(f"Remove the value 1 : {myset}")

myset.discard(5)
print(f"Discard the value 5 : {myset}")

myset.pop()     ###########  Remove the value randomly
print(f"Pop up the value : {myset}")

myset.clear()       #########  Delete all values from the set
print(f"Clear the set : {myset}")       #######     Output:set()

# del myset         #########   Delete the set completely
# print(f"Delete the value : {myset}")