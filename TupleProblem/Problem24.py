########    Check if an element exists in a tuple.

mytup = ("apple", "lich", "grap", "orange")
if "apple" in mytup:
    print("Apple is in the tuple")
else:
    print("Apple is not in the tuple")

for i in mytup:
    if "apple" in i:
        break
    else:
        print("Apple is not in the tuple")

print("Apple is in the tuple")

# # ##########3 any() ← this is correct, not all()
# # # any() = True if AT LEAST ONE match found
if any(x == "grap" for x in mytup):
    print("Grap is in the tuple")
#
# #############   for loop manually
# found = False
# for x in mytup:
#     if x == "grap":
#         found = True
#         break           # stop searching once found
#
# print("My tuple is ", "Found!" if found else "Not found!")
#
# # # count() built-in
# # # count() counts how many times element appears
# # # if count > 0 → element exists
# if mytup.count("lich") > 0:
#     print("My tuple is Found!")
#
# mytup = ("apple", "lich", "grap", "orange")
target = "apple"
#
# # all() way — checks if element is NOT different from target
# # in other words — if any element MATCHES target
result = not all(x != target for x in mytup)
#                  ↑
#         "is every element NOT apple?"
#         if False for even one → apple exists!

if result:
    print("Apple is in the tuple")
else:
    print("Apple is not in the tuple")

# ########    Using Index
# print(f"{mytup.index("grap")} is found in my tuple")

########    Tuple to Set e convert
# myset = set(mytup)
# if "apple" in mytup:
#     print("Apple is in the tuple")
# else:
#     print("Apple is not in the tuple")

##########  Using any()
# if any(x == "grap" for x in myset):
#     print("Grap is in the set")

##########  Using all()
# if not all(x != "grap" for x in myset):
#     print("Grap is in the set")


