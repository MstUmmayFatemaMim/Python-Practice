# #Show difference between assignment and copy for lists.
# a = [1, 2, 3]
# b = a            # b points to same list
# b.append(4)
# print("Assignment : ")
# print(a)  # [1, 2, 3, 4]  ← a changed! 😱
# print(b)  # [1, 2, 3, 4]
#
# a = [1, 2, 3]
# b = a.copy()    # b is a brand new list
# b.append(4)
# print("Copy : ")
# print(a)         # [1, 2, 3]      ← a is safe!
# print(b)         # [1, 2, 3, 4]
from DictionariesProblem.Problem1 import student

# # Show difference between assignment and copy for tuples.
# ## Assign the value
# a=(1,2,3,4)     #create variable
# b=a         #assign in b
# print(a,b)
# print(id(a),id(b))
# b+=(99,)
# print(a,b)
# print(id(a),id(b))
# ### Copy the value
# a=(3,5,62,5)
# # b=tuple(a)        # copy the tuple way 1
# b=a[:]             ## copy the tuple way 2
# print(a,b)
# print(id(a),id(b))
# b += (99,)
# print(a, b)
# print(id(a), id(b))

# # Show difference between assignment and copy for sets.
# # ## Assign the value
# a={1,2,3,4}    #create variable
# b=a         #assign in b or reference deya
# print(a,b)
# print(id(a),id(b))
# a.add(333)
# print(a,b)
# print(id(a),id(b))
# ## Copy the value
# c={3,5,62,5}
# d=c
# print(c,d)
# print(id(c),id(d))
# c.add(44)
# print(c,d)
# print(id(c),id(d))

# Show difference between assignment and copy for dictionary.
# ## Assign the value
student = {
    "name":"Mim",
    "age":24
}
person=student      ##assign value does not change the memory location
print(student,person)
print(id(student),id(person))

####Copy the dictionary
person=student.copy()
print(id(student),id(person))       ##copy value change the memory
