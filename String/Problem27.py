#################       Find the longest word in a sentence.

text="Hello World from Bangladesh"
word=text.split()
print(word)
text1=len(word)
print(text1)
# i=0
# while i<text1:
#     print(word[i])
#     i=i+1

for i in range(len(word)):
    count=0
    for j in range(len(word[i])):
        count=count+1
    print(word[i],count,end=" ")
print()
longest_word=word[0]
for i in range(len(word)):
    if len(word[i])>len(longest_word):
        longest_word=word[i]
print(longest_word)