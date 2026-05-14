########Reverse a string without using slicing ([::-1]).
name="name"
i=len(name)-1
nam=[]
while i>=0:
    nam.append(name[i])
    i=i-1
print(nam)