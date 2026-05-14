#######Count the number of vowels in a string.

name="name"
count=0
i=0
while i<len(name):
    if name[i] in 'aeiouAEIOU':
        count+=1
    i=i+1
print(count)