# ############    116. Dictionary Value Sharing Bug
# Write code where:
# Multiple dictionary keys share the same list
# Modifying one affects all
#  Then fix it.
shared = []
d = {"a": shared, "b": shared}
d["a"].append(1)
print(d)

d_fixed = {"a": [], "b": []}  # Or {"a": shared.copy(), "b": shared.copy()}
d_fixed["a"].append(1)
print(d_fixed)


#########   Fix the Dictionary Bug (your shared = [] code)
# shared = []
#
# # ❌ BUGGY — both keys share same list
# d = {"a": shared, "b": shared}
# d["a"].append(1)
# print(d)    # {"a": [1], "b": [1]} 😱 both changed!
#
#
# # ✅ FIX 1 — give each key its own copy
# shared = []
# d = {"a": shared.copy(),    # NEW box for "a"
#      "b": shared.copy()}    # NEW box for "b"
#
# d["a"].append(1)
# print(d)    # {"a": [1], "b": []} ✅ only "a" changed!
#
#
# # ✅ FIX 2 — use list() to create independent copies
# shared = []
# d = {"a": list(shared),     # NEW box for "a"
#      "b": list(shared)}     # NEW box for "b"
#
# d["a"].append(1)
# print(d)    # {"a": [1], "b": []} ✅
#
#
# # ✅ FIX 3 — use deepcopy (best for nested lists)
# import copy
# shared = [1, 2, 3]
# d = {"a": copy.deepcopy(shared),
#      "b": copy.deepcopy(shared)}
#
# d["a"].append(99)
# print(d)    # {"a": [1,2,3,99], "b": [1,2,3]} ✅
