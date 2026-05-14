####Count how many times a character appears in a string.
# s1="mimim"
# seen=[]               #####   Problem
# i=0
# count=0
# while i<len(s1):
#     if s1[i] in seen:     ####### This logic work for one element
#         count+=1
#     else:
#         seen.append(s1[i])
#     i+=1
# print(count)


m="mimimim"
i=0
count={}
while i<len(m):
    char=m[i]       ##### # .lower() turns capital 'M' or 'I' into small 'm' or 'i' ****** char = m[i].lower()
    if char in count:
        count[char]+=1
    else:
        count[char]=1
    i+=1
print(count)