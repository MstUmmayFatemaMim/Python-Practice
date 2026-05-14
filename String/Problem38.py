#############   Check if a string follows the pattern "abba" → "dog cat cat dog".

pattern = "abba"
string = "dog cat cat dog"

words = string.split()
mapping = {}

for i in range(len(pattern)):
    letter = pattern[i]
    word = words[i]

    if letter not in mapping:
        mapping[letter] = word  # first time seeing 'a' → store 'dog'
    else:
        if mapping[letter] != word:  # second time seeing 'a' → must match
            print("Not matched")
            break
else:
    print("Matched")


# pattern = "abba"
# string = "dog cat cat dog"
#
# words = string.split()   # ['dog', 'cat', 'cat', 'dog']
#
# # Check every pattern letter against every word
# match = True
#
# for i in range(len(pattern)):
#     for j in range(len(pattern)):
#         if (pattern[i] == pattern[j]) != (words[i] == words[j]):
#             match = False
#
# print(match)  # True