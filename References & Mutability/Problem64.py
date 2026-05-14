# ######## Shallow copy problem       .copy() only copies the outer list — the inner lists are still shared!
###Demonstrate shallow copy problem with nested lists.

# a = [[1, 2], [3, 4]]
# b = a.copy()           # looks safe...
# b[0].append(99) #It shares the inner object
# b.append([5, 6]) #It does not share.the outer object. *** If I want to share this,I need to use deep copy.
# print(a)   # [[1, 2, 99], [3, 4]]  ← a changed!
# print(b)    # [[1, 2, 99], [3, 4]]

###########Method 8 — prove it with id() — see memory address
# a = [[1, 2], [3, 4]]
# b = a.copy()
# print(id(a),id(b))  #memory address changed
# print(id(a) == id(b))      # False  ← different outer lists
# print(id(a[0]) ,id(b[0]))
# print(id(a[0]) == id(b[0]))# True   ← same inner list!
# print(id(a[1]) == id(b[1]))# True   ← same inner list!
# ##########Method 2 — [:] slice on nested list
# a = [[1, 2], [3, 4]]
# b = a[:]              # same problem as .copy()
# b[0].append(99)
# print(a)  # [[1, 2, 99], [3, 4]]  ← a changed! 😱
# print(b)  # [[1, 2, 99], [3, 4]]
#
# ############Method 3 — list() constructor on nested list
# a = [[1, 2], [3, 4]]
# b = list(a)           # still shallow!
# b[0].append(99)
# print(a)  # [[1, 2, 99], [3, 4]]  ← a changed! 😱
# print(b)  # [[1, 2, 99], [3, 4]]
#
# ########## Method 4 — nested list inside a dictionary
# data   = {"scores": [10, 20, 30]}
# backup = data.copy()         # dict shallow copy
# backup["scores"].append(99)
# print(data["scores"])    # [10, 20, 30, 99]  ← changed! 😱
# print(backup["scores"])  # [10, 20, 30, 99]
#
# ###########Method 5 — 3 levels deep (triple nested)
# a = [[[1, 2], [3, 4]], [[5, 6]]]
# b = a.copy()
# b[0][0].append(99)         # going 2 levels deep
# print(a)  # [[[1, 2, 99], [3, 4]], [[5, 6]]]  ← a changed! 😱
# print(b)  # [[[1, 2, 99], [3, 4]], [[5, 6]]]
#
# ##############Method 6 — copy.copy() from module (same problem)
# import copy
# a = [[1, 2], [3, 4]]
# b = copy.copy(a)      # copy.copy = shallow copy, same problem!
# b[1].append(99)
# print(a)  # [[1, 2], [3, 4, 99]]  ← a changed! 😱
# print(b)  # [[1, 2], [3, 4, 99]]
#
# ###########Method 7 — unpacking [*a] on nested list
# a = [[1, 2], [3, 4]]
# b = [*a]              # unpack — also shallow!
# b[0].append(99)
# print(a)  # [[1, 2, 99], [3, 4]]  ← a changed! 😱
# print(b)  # [[1, 2, 99], [3, 4]]

# # Fix — use deepcopy        the inner lists are not shared!
# import copy
# a = [[1, 2], [3, 4]]
# b = copy.deepcopy(a)   # copies everything
# b[0].append(99)
# print(a)   # [[1, 2], [3, 4]]
# print(id(a))    #memory address changed
# print(b)   # [[1, 2, 99], [3, 4]]
# print(id(b))    #memory address changed

###Demonstrate shallow copy problem with nested tuples.

# import copy
# a = (9, [1, 2], [3, 4])
# b = copy.copy(a)
# # The "Problem": Modifying a nested list in 'b' affects 'a'
# b[1].append(99)
# print(a) # Output: (9, [1, 2, 99], [3, 4]) -- IT CHANGED!
# print(b) # Output: (9, [1, 2, 99], [3, 4])

# ###Demonstrate shallow copy problem with nested sets.
# a = {1, frozenset({2, 3}), 4}
# new=set(a)
# print(new)
# print(a)
# a.add(8)
# print(a)
# print(id(a), id(new))

###Demonstrate shallow copy problem with nested dictionary.
# import copy
# student = {
#     "name":"Mim",
#     "age":24
# }
# print(student)
# person=copy.copy(student)
# print(person)
# person["bname"]="Mim"
# print(person)