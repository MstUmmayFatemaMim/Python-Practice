# # #############3Write code that proves rebinding ≠ modification.
# # #
# ┌─────────────────────────────────────────────────────────┐
# │              REBINDING vs MODIFICATION                  │
# ├─────────────────────────┬───────────────────────────────┤
# │      REBINDING          │       MODIFICATION            │
# ├─────────────────────────┼───────────────────────────────┤
# │ x = [1,2,3]             │ x = [1,2,3]                   │
# │ x = [4,5,6]  ← নতুন    │ x.append(4) ← একই box        │
# │                         │                               │
# │ address বদলায় ✅        │ address একই থাকে ✅           │
# │ পুরনো object অক্ষত ✅   │ পুরনো object বদলায় ⚠️        │
# │ অন্য variable safe ✅   │ অন্য variable ও বদলায় ⚠️     │
# ├─────────────────────────┼───────────────────────────────┤
# │ lst = []                │ lst.append()                  │
# │ lst = lst + [1]         │ lst.extend()                  │
# │ lst = [*lst, 1]         │ lst.insert()                  │
# │ lst = list(lst)         │ lst[0] = 99                   │
# │ num = num + 1           │ lst += [1] (list only)        │
# └─────────────────────────┴───────────────────────────────┘
# # MODIFICATION (পরিবর্তন):
# # → একই box এর ভেতরের জিনিস বদলাও
# # → box এর address একই থাকে
#
# ######## Using list
# a=[2,3,5,7,9]
# b=a
# print(a==b)
# print(id(a) , id(b))
# b.append(10)
# print(id(a) , id(b))
# print(a==b)
# print(a)
# print(b)

########## Using Tuples
# a=(2,[3,5],7,9)
# b=a
# print(a==b)
# print(id(a) , id(b))
# b[1].append(90)
# print(id(a) , id(b))
# print(a==b)
# print(a,b)

# ######### Using Dictionary
# student={
#     "name":"Mim",
#     "age":24
# }
# person=student
# print(person,student)
# person["bnam"]="Mimi"
# print(person,student)
# print(id(person),id(student))

# REBINDING (নতুন নাম দেওয়া):
# → পুরনো box ফেলে নতুন box ধরো
# → address বদলে যায়
# x=[4,5,6]
# y=x
# print(x == y)
# print(id(x) , id(y))
#
# x=[7,9,8,3]
# print(x == y)  ###it does not reassign here.So show false
# print(id(x) , id(y))

# ########## Using Tuples
# a=(2,[3,5],7,9)
# b=a
# print(a==b)
# print(id(a) , id(b))
# a=(24,[33,5],7,99)
# print(a==b)
# print(a,b)

######### Using Dictionary
student={
    "name":"Mim",
    "age":24
}
person=student
print(person,student)

student={
    "address":"<UNK>",
    "city":"<UNK>",
    "country":"<UNK>"
}
print(person,student)
print(id(person),id(student))
print(person==student)
#
# def prove_rebinding(lst):
#     print("Inside - Before rebind:", id(lst))
#     lst = [99, 88, 77]               # local rebinding
#     print("Inside - After rebind:", id(lst))
#     return lst
#
# def prove_modification(lst):
#     print("Inside - Before modify:", id(lst))
#     lst.append(99)                   # actual modification
#     print("Inside - After modify:", id(lst))
#     return lst

# # ============ REBINDING TEST ============
# my_list = [1, 2, 3]
# print("Outside before:", id(my_list))
# result = prove_rebinding(my_list)
# print("Outside after:", id(my_list))
# print("my_list =", my_list)          # অক্ষত! rebinding বাইরে affect করে না
# print("result  =", result)
# print()
#
# # ============ MODIFICATION TEST ============
# my_list2 = [1, 2, 3]
# print("Outside before:", id(my_list2))
# result2 = prove_modification(my_list2)
# print("Outside after:", id(my_list2))
# print("my_list2 =", my_list2)        # বদলে গেছে! modification বাইরেও affect করে
# print("result2  =", result2)

# Integer → Immutable → সবসময় rebinding হয়
# List    → Mutable   → modification সম্ভব
#
# # ============ INTEGER (Rebinding always) ============
# num = 5
# print("int before:", id(num))   # address: 9000
#
# num = num + 1                   # নতুন int তৈরি হয়
# print("int after:", id(num))    # address: 9001 ← DIFFERENT!
# print()
#
# # ============ LIST (Modification possible) ============
# lst = [1, 2, 3]
# print("list before:", id(lst))  # address: 140001
#
# lst.append(4)                   # same list modify করো
# print("list after:", id(lst))   # address: 140001 ← SAME!
# print()
#
# # ============ LIST REBINDING ============
# lst2 = [1, 2, 3]
# print("list2 before:", id(lst2))  # address: 140002
#
# lst2 = [1, 2, 3, 4]              # নতুন list এ rebind করো
# print("list2 after:", id(lst2))   # address: 140003 ← DIFFERENT!