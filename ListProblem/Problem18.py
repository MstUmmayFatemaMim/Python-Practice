list1=[1,2,3,4,5,6,7,8,9]
list2=[11,22,33,44,5,6,7,8,9]
list3=[]
for x in list1:
    for y in list2:
        if x==y:
            list3.append(x)
print(list3)