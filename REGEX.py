import re
#RegEx can be used to check if a string contains the specified search pattern.
#Check if the string starts with "The" and ends with "Spain":
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt) ##checking work
#
# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")

# txt = "The rain in Spain"
# x = re.search("ai", txt)
#
# print(x)                    # output: <...span=(5, 7), match='ai'>
# print(x.span())             # output: (5, 7)
# print(x.start())            # output: 5  ← শুরু
# print(x.end())              # output: 7  ← শেষ
# print(x.group())            # output: ai ← কী পাওয়া গেছে
# print(txt[5:7])             # output: ai ← prove! ✅
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())