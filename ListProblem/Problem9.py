# Swap the first and last element of a list.
newlist= [50, 30, 70, 190, 500, 200]
temp=newlist[0]
newlist[0]=newlist[len(newlist)-1]
newlist[len(newlist)-1]=temp
print(newlist)