##########Show default argument list problem.

# # # Method 1 — None as Default Sentinel
# def append_item(item, lst=[]):
#     lst.append(item)
#     return lst
#
# print(append_item(1))
# print(append_item(2))
# print(append_item([1,4,5]))

######### extend
def append_item(lst=[]):      # একটাই parameter — পুরো list নেবে
    result = []               # fresh empty list বানাও
    for item in lst:          # lst এর প্রতিটা item ধরো
        if isinstance(item, list):   # item যদি list হয়
            result.extend(item)      # list কে ভেঙে একে একে add করো
        else:                        # item যদি number হয়
            result.append(item)      # সরাসরি add করো
    return result             # final list return করো

print(append_item([1, 2, [1,4,5]]))  # [1, 2, 1, 4, 5]  ✅ flat list