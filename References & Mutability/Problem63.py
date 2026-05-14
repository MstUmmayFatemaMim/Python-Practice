# # #Write code where modifying one list does not affect another.
# a = [1, 2, 3]
# b = a.copy()     # brand new list
# b.append(99)
# print(a)  # [1, 2, 3]
# print(b)  # [1, 2, 3, 99]

# ##############Method 2 — [:] slice — old school trick
#
# a = [1, 2, 3]
# b = a[:]        # slice from start to end = everything
# b.append(99)
# print(a)  # [1, 2, 3]       
# print(b)  # [1, 2, 3, 99]
#
# #########Method 3 — list() constructor
#
# a = [1, 2, 3]
# b = list(a)     # wraps a into a new list object
# b.append(99)
# print(a)  # [1, 2, 3]       ← safe! ✅
# print(b)  # [1, 2, 3, 99]
#
# ############# Method 4 — list comprehension
#
# a = [1, 2, 3]
# b = [x for x in a]   # loops through a, builds brand new list
# b.append(99)
# print(a)  # [1, 2, 3]       ← safe! ✅
# print(b)  # [1, 2, 3, 99]
#
# ###########Method 5 — copy.copy() from the copy module
# import copy
# a = [1, 2, 3]
# b = copy.copy(a)   # same as a.copy() but from the module
# b.append(99)
# print(a)  # [1, 2, 3]
# print(b)  # [1, 2, 3, 99]
#
# ##############Method 6 — copy.deepcopy() — for nested lists
# import copy
# a = [[1, 2], [3, 4]]
# b = copy.deepcopy(a)   # copies outer AND inner lists
# b[0].append(99)
# print(a)  # [[1, 2], [3, 4]]
# print(b)  # [[1, 2, 99], [3, 4]]

# #######Method 7 — * unpacking into new list
# a = [1, 2, 3]
# b = [*a]        # unpack all elements of a into a new list
# b.append(99)
# print(a)  # [1, 2, 3]       ← safe! ✅
# print(b)  # [1, 2, 3, 99]

# ##########Method 8 — copy inside function — protect original from changes
# def add_item(lst):
#     lst = lst.copy()    # make a local copy first
#     lst.append(99)
#     return lst
# a = [1, 2, 3]
# b = add_item(a)
# print(a)  # [1, 2, 3]       ← safe! ✅
# print(b)  # [1, 2, 3, 99]

# # #Write code where modifying one tuple does not affect another.
# a=(1,2,3,4)     #create variable
# b=list(a)        #assign in b
#
# b.append(99)    ######After changing it does not affect
# print(a,b)
# print(id(a),id(b))
# b=tuple(b) ####Convert the tuple
# print(a,b)

# # #Write code where modifying one set does not affect another.
#
# a={1,2,3,4}     #create variable
# b=set(a)    #copy the value
# b.add(99)    ######After changing it does not affect
# print(a,b)
# print(id(a),id(b))

# #Write code where modifying one dictionary does not affect another.
student = {
    "name":"Mim",
    "age":24
}
person=dict(student)      ##assign value does not change the memory location
print(student,person)
print(id(student),id(person))
person["address"]="Dhaka"
print(person,student)
print(id(student),id(person))
