# Remove all duplicate values from a list.
newlist5=[50,30,70,190,500,200,50,30]
newlist5.sort()
# print(newlist4)
i=0
while i<len(newlist5)-1:
    if(newlist5[i+1]==newlist5[i]):
        newlist5.pop(i+1)
    i=i+1
print(newlist5)