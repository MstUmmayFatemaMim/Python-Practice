#########   Remove empty strings from a list.
words = ["apple", "", "banana", "", "mango", "  ", "", "grape"]
result = []
for word in words:
    if word != "" or "  ":
        result.append(word)
print(result)

# ########### Way 2 — Using strip() to also remove space-only strings
# result = []
# for word in words:
#     if word.strip() != "":     # strip() removes spaces first, then check
#         result.append(word)
# print(result)

# # Only removes ""
# result = [word for word in words if word != ""]
#
# # Also removes "  " (space-only)
# result = [word for word in words if word.strip()]
#
# print(result)

# ############    Way 4 — Using filter() (functional style)
# result = list(filter(str.strip, words))   # str.strip acts as the condition
# print(result)
#
# ###########     Way 5 — Using remove() in a loop (modifies original list)
# words = ["apple", "", "banana", "", "mango", "  ", "", "grape"]
# while "" in words:
#     words.remove("")       # removes one "" at a time until none left
# print(words)

# ###########     Way 6 — Using join() + split() trick (fun one-liner)
# result = " ".join(words).split()
# print(result)