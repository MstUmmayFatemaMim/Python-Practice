######Extract only digits from a string.
m="Mim88im178@im"
count2=0
i=0
while i<len(m):
    if m[i] in '1234567890':
        count2+=1

    i+=1

print(count2)