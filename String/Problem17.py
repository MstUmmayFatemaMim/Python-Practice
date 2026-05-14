#######Find all duplicate characters in a string.
m="messamage"
i=0
count={}
while i<len(m):
    char=m[i]       ##### # .lower() turns capital 'M' or 'I' into small 'm' or 'i' ****** char = m[i].lower()
    if char in count:
        count[char]+=1
    else:
        count[char]=1
    i+=1
print(f"Count the every character: {count}")

for char in count:
    if count[char]>=2:
        print(f"Duplicated character: {char}")