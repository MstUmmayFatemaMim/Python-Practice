########## Create a list of numbers from 1 to 10 and print only the even numbers.
newlist=[]
i=1
while i<=10:
    if i%2==0:
        newlist.append(i)
    i=i+1
print(newlist)