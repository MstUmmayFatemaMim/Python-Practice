# ###########      119. Snapshot vs Live Data
# Write a function that:
# Returns a “snapshot” of a list
# And another that returns a “live reference”
# Demonstrate the difference.

# Snapshot data means static data

def get_data():
    return list1.copy()

print("Live Reference : ")
list1=[1,2,4,7,9]
list2=get_data()
list2.append(8)
print(list1)
print(list2)

def get_data():
    return list3
print("Snapshot Reference : ")
list3=[1,2,4,7,9]
list3.append(89)
print(list3)
list4=get_data()
print(list4)