##########      Find first non-repeating character in a string
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
print(count)

for char in count:
    if count[char]==1:
        print(char)


# #########       This works for sentence non repeating word
# text="my name is mimi"
# words=text.split()
# count = {}
# for word in words:
#     # count[word] = count.get(word, 0) + 1
#     # The long way without get()
#     if word in count:
#         count[word] += 1
#     else:
#         count[word] = 1
#
# print("Count:", count)
#
# # Step 2 — find first non-repeating word
# for word in words:
#     if count[word] == 1:
#         print("First non-repeating word:", word)
#         break