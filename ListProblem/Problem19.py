###########     Check if a list is a palindrome.

# list1=[1,2,3,4,5,6,7,8,9]
list1=[1,2,2,2,1]

list3=[]
i=len(list1)
while i>0:
    list3.append(list1[i-1])
    i=i-1

if list3== list1:
     print("It is palindrome")
else:
     print("It is not palindrome")
###########     *******     Wrong Code  ***************
# list1.reverse()
# if list1==list1.reverse():
#     print("It is palindrome")
# else:
#     print("It is not palindrome")
# # original list1 = [1, 2, 2, 2, 1]
# # # # step 1 → list1.reverse()
# # # #          list1 is now = [1, 2, 2, 2, 1]  ← same (palindrome!)
# # # #          but original is gone!
# # # # step 2 → list1 == list1.reverse()
# # # #          list1 == None
# # # #          [1,2,2,2,1] == None → False ❌
# # # # prints "It is not palindrome" ← wrong!

# list1 = [1, 2, 2, 2, 1]
# list1=[1,2,3,4,5,6,7,8,9]

# ─────────────────────────────────────────
# Way 1 — slicing (easiest and cleanest)
# [::-1] means reverse the list
# ─────────────────────────────────────────
# if list1 == list1[::-1]:      # compare original with reversed copy
#     print("It is palindrome")
# else:
#     print("It is not palindrome")

#
# # ─────────────────────────────────────────
# # Way 2 — save reversed in a new variable
# # ─────────────────────────────────────────
# list1 = [1, 2, 2, 2, 1]
# reversed_list = list1.copy()  # copy first
# reversed_list.reverse()       # reverse the copy
#
# if list1 == reversed_list:    # compare original with reversed copy
#     print("It is palindrome")
# else:
#     print("It is not palindrome")
#
#
# # ─────────────────────────────────────────
# # Way 3 — using reversed() built-in
# # reversed() returns reversed copy without changing original
# # ─────────────────────────────────────────
# list1 = [1, 2, 2, 2, 1]
# if list1 == list(reversed(list1)):
#     print("It is palindrome")
# else:
#     print("It is not palindrome")
#
# #
# # # ─────────────────────────────────────────
# # # Way 4 — manual loop (most basic)
# # # compare first and last, second and second last...
# # # ─────────────────────────────────────────
# list1 = [1, 2, 2, 2, 1]
# is_palindrome = True
#
# for i in range(len(list1) // 2):
#     if list1[i] != list1[-(i+1)]:   # compare from both ends
#         is_palindrome = False
#         break
#
# print("It is palindrome" if is_palindrome else "It is not palindrome")