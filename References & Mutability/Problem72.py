###########Fix default argument problem.
#
# def append_item(item, n=5):
#     n=n+item
#     return n
#
# print(append_item(1))
# print(append_item(2))
# print(append_item(1))
#
###########3 fix it list
# def append_item(item, n=[]):
#     n.append(item)
#     return n
#
# print(append_item(1))
# print(append_item(2))
# print(append_item(1))

# def append_item(item, n=()):
#     n.add(item)
#     return n
#
# new=(3,4,2)
# print(append_item(new))
def append_item(item, n=()):
    return n + item # No comma needed if 'item' is already a tuple

new = (3, 4, 2)
print(append_item(new))
# Output: (3, 4, 2)

# #########Using lambda
# append_item = lambda item, n=5: n + item   # এক লাইনে পুরো function
#
# print(append_item(1))         # 6  ✅
# print(append_item(2))         # 7  ✅
# print(append_item(1))         # 6  ✅
# print(append_item(1, 10))     # 11 ✅
# print(append_item(2, 20))     # 22 ✅

# def append_item(item, *args):
#     n = args[0] if args else 5    # args এ কিছু থাকলে নাও, নাহলে 5
#     return n + item               # যোগ করে return করো
#
# print(append_item(1))             # 5 + 1 = 6  ✅
# print(append_item(2))             # 5 + 2 = 7  ✅
# print(append_item(1))             # 5 + 1 = 6  ✅
#
# # Custom n দিলেও কাজ করে
# print(append_item(1, 10))         # 10 + 1 = 11 ✅
# print(append_item(2, 20))         # 20 + 2 = 22 ✅
#
# # *args
# # │
# # └── extra arguments গুলো tuple এ collect করে
# #     append_item(1)     → args = ()     ← খালি
# #     append_item(1, 10) → args = (10,)  ← 10 আছে
# #
# # args[0] if args else 5
# # │           │         │
# # │           │         └── args খালি হলে 5 নাও
# # │           └── args এ কিছু আছে কিনা check
# # └── প্রথম extra argument নাও

# def append_item(item, **kwargs):
#     n = kwargs.get('n', 5)    # 'n' key আছে? নিলে নাও, নাহলে 5
#     return n + item
#
# print(append_item(1))          # 6  ✅
# print(append_item(2))          # 7  ✅
# print(append_item(1))          # 6  ✅
#
# # Custom n দিলেও কাজ করে
# print(append_item(1, n=10))    # 11 ✅
# print(append_item(2, n=20))    # 22 ✅
#
# # **kwargs
# # │
# # └── named arguments গুলো dictionary তে collect করে
# #     append_item(1)       → kwargs = {}          ← খালি
# #     append_item(1, n=10) → kwargs = {'n': 10}   ← n আছে
# #
# # kwargs.get('n', 5)
# # │     │    │   │
# # │     │    │   └── না পেলে default 5
# # │     │    └── 'n' key খোঁজো
# # │     └── dictionary method
# # └── kwargs dictionary