##########Count the number of consonants in a string.

name="names"
count=0
i=0
while i<len(name):
    if name[i] not in 'aeiouAEIOU' :
        count+=1
    i=i+1
print(count)