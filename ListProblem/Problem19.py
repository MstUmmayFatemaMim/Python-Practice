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