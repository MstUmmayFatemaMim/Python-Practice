#####Check if two strings are anagrams.
text="listen"
ntext="silent"

for i in text:
    for j in ntext:
        if i == j:
            break

if len(text)==len(ntext):
    print("Anagram")
else:
    print("Not Anagram")