newlist= [50, 30, 70, 190, 500, 200,60]
# n=newlist[::-1] # left to right
# n1=n[::-1] # right to left
# print(n)
# print(n1)

# i=len(newlist)-1
# while i>=0:
#     if newlist[i]==newlist[0]:
#     newlist.append(newlist[0])
#     break
#     i=i-1
# newlist1=newlist[1:]
# newlist2=newlist + newlist1
# print(newlist2)
#
# newlist2 = newlist[-1:]
# newlist3 = newlist[:1]
# print(newlist2)
# print(newlist3)

mylist = [1, 2, 3, 4, 5]

# ১ ঘর Left rotate
rotated = mylist[2:] + mylist[:2]
print(rotated)