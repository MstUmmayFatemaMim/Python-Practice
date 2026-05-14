#####       Find the longest substring without repeating characters.

text = "abcabcbb"

longest = ""

for start in range(len(text)):
    current = ""
    for end in range(start, len(text)):
        letter = text[end]
        if letter not in current:
            current += letter           # keep expanding
        else:
            break                       # stop when repeat found

    if len(current) > len(longest):
        longest = current

print("Longest:", longest)
print("Length:", len(longest))


# text = "abcabcbb"
#
# seen = set()
# left = 0
# longest = ""
#
# for right in range(len(text)):
#     while text[right] in seen:
#         seen.remove(text[left])         # shrink from left
#         left += 1
#
#     seen.add(text[right])
#     current = text[left:right+1]
#
#     if len(current) > len(longest):
#         longest = current
#
# print("Longest:", longest)
# print("Length:", len(longest))

# text = "abcabcbb"
#
# seen = {}
# start = 0
# longest = ""
#
# for i in range(len(text)):
#     letter = text[i]
#
#     if letter in seen and seen[letter] >= start:
#         start = seen[letter] + 1        # move start forward
#
#     seen[letter] = i                    # update letter's index
#     current = text[start:i+1]
#
#     if len(current) > len(longest):
#         longest = current
#
# print("Longest:", longest)
# print("Length:", len(longest))