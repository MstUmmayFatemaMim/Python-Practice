###########     Find common characters between two strings using sets.
word = "Women"
word1 = "Men"
set1 = set(word.lower())
set2 = set(word1.lower())
common_chars = set1 & set2
print(common_chars)

# word = "Women"
# word1 = "Men"
#
# newset = set()
# word = word.lower()
# word1 = word1.lower()
#
# for char in word:
#     if char in word1:
#         newset.add(char)
#
# print(newset)




