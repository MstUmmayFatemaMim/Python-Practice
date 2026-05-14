# ######## new object is false. same object is true.
# ##### same value == true. updated value == false
#
# ###############Method 1 — assignment is and == both True
#
# # a = [1, 2, 3]
# # b = a             # b points to same object
# # print(a == b)     # True  ✅ same values
# # print(a is b)     # True  ✅ same object in memory
# # print(id(a) == id(b))  # True — same address
#
# ###########Method 2 — .copy() == True but is False
# a = [1, 2, 3]
# b = a.copy()      # brand new list, same values
# print(a == b)     # True  ✅ same values
# print(a is b)     # False ❌ different objects
# print(id(a) == id(b))  # False — different addresses
#
# ############Method 3 — list() constructor == True but is False
# a = [1, 2, 3]
# b = list(a)       # new list object
# print(a == b)     # True  ✅ same values
# print(a is b)     # False ❌ different objects
#
# #############Method 4 — [:] slice == True but is False
# a = [1, 2, 3]
# b = a[:]          # slice = new list
#
# print(a == b)     # True  ✅ same values
# print(a is b)     # False ❌ different objects ******* b has all the same elements, it lives at a different memory address.

# ###########Method 5 — two separate lists same values
# a = [1, 2, 3]
# b = [1, 2, 3]     # written separately --> creates two separate list objects in memory.
#
# print(a == b)     # True  ✅ same values
# print(a is b)     # False ❌ different objects


# ############Method 6 — different values == and is both False
# a = [1, 2, 3]
# b = [1, 2, 99]    # different value
# ###When values differ, both == and is are False.
# print(a == b)     # False ❌ different values
# print(a is b)     # False ❌ different objects

# ##############Method 7 — after modifying, == becomes False but is stays same
# a = [1, 2, 3]
# b = a             # same object
#
# print(a is b)     # True  ✅
# print(a == b)     # True  ✅
#
# b.append(99)      # modify through b
#
# print(a is b)     # True  ✅ still same object
# print(a == b)     # True  ✅ still equal (same object!)
# print(a)          # [1, 2, 3, 99]
#
# ##############Method 8 — is None — the right way to check None
# a = None
# # ✅ Correct way — use is
# if a is None:
#     print("a is None")   # prints this
# # ⚠️ Works but not recommended ***Always use is None not == None
# if a == None:
#     print("a equals None")
# # Why is is better?
# # None is a singleton — only ONE None object exists in Python
# # is checks that directly without calling __eq__


##########Method 9 — prove with id() fully      id() makes it crystal clear — is is literally checking if id(a) == id(b).
a = [1, 2, 3]
b = a
c = a.copy()
d = [1, 2, 3]

print(id(a))   # e.g. 140100
print(id(b))   # 140100 ← same as a!
print(id(c))   # 140200 ← different
print(id(d))   # 140300 ← different

print(a is b)  # True  — same id
print(a is c)  # False — different id
print(a is d)  # False — different id

print(a == b)  # True
print(a == c)  # True
print(a == d)  # True  — all have same values