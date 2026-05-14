######Count digits, letters, and special characters in a string.
m="Mim88im@im"
count=0
count2=0
count3=0
i=0
while i<len(m):
    if m[i].lower() in 'abcdefghijklmnopqurstuvwxyz':
        count+=1
    elif m[i] in '1234567890':
        count2+=1
    else:
        count3+=1
    i+=1

print(count,count2,count3)