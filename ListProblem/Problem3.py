######## Reverse a list without using .reverse() or slicing.

newlist2=[10,20,30,40,50]
newlist3=[]
i=len(newlist2)-1
while i>=0:
    newlist3.append(newlist2[i])
    i=i-1
print(newlist3)