#######Write a function that counts vowels in a string.
def vowel_counter(n):
    count = 0
    for letter in n:
        if letter in 'aeiouAEIOU':
            count += 1
    return count

name="My name is eiAUeiou"
print(vowel_counter(name))

# ###########Method 2 — lower() to handle uppercase cleanly
# def count_vowels(s):
#     count = 0
#     s = s.lower()          # convert whole string to lowercase first
#     for ch in s:
#         if ch in "aeiou":  # now only check 5 vowels
#             count += 1
#     return count
#
# print(count_vowels("HELLO WORLD"))   # 3

###########Method 3 — sum() with generator — one liner
# def count_vowels(s):
#     return sum(1 for ch in s if ch.lower() in "aeiou")
#                 # "Hello World"
#                 # → for each ch: H e l l o   W o r l d
#                 # → is it a vowel?  N Y N N Y N Y N N N
#                 # → sum of 1s:      0+1+0+0+1+0+1+0+0+0 = 3
# print(count_vowels("Hello World"))   # 3

# ################Method 4 — filter() functional style
# def count_vowels(s):
#     return len(list(filter(lambda ch: ch.lower() in "aeiou", s)))
# # filter(lambda ch: ch.lower() in "aeiou", s)       #filter() pass the value
# #          ↓
# # keeps only vowel characters → ['e', 'o', 'o']
# #          ↓
# # len([...]) → 3
# print(count_vowels("Hello World"))   # 3

# ######################Method 5 — count() for each vowel
# def count_vowels(s):
#     s = s.lower()
#     return sum(s.count(v) for v in "aeiou")
#
# print(count_vowels("Hello World"))   # 3

# ##################Method 6 — set intersection — smartest approach
# def count_vowels(s):
#     vowels = set("aeiouAEIOU")
#     return sum(1 for ch in s if ch in vowels)
# # Why set is faster:
# # python# Checking ch in "aeiouAEIOU" → scans string left to right (slow)
# # # Checking ch in {set}        → instant hash lookup (fast)
# print(count_vowels("Hello World"))   # 3

################Method 7 — re (regex) — most powerful
# import re
#
# def count_vowels(s):
#     return len(re.findall(r"[aeiouAEIOU]", s)) ###[aeiouAEIOU] is a character class — matches any single vowel. Most powerful for complex pattern matching.
# # How it works:
# # pythonre.findall(r"[aeiouAEIOU]", "Hello World")
# # → finds all characters matching the pattern
# # → ['e', 'o', 'o']
# # → len(['e', 'o', 'o']) = 3
# print(count_vowels("Hello World"))   # 3


##########Method 8 — Counter from collections — shows each vowel count
# from collections import Counter
#
# def count_vowels(s):
#     counts = Counter(ch.lower() for ch in s)
#     return sum(counts[v] for v in "aeiou")
#
# print(count_vowels("Hello World"))   # 3
#
# # Bonus — see each vowel separately:
# def vowel_breakdown(s):
#     counts = Counter(ch.lower() for ch in s)
#     return {v: counts[v] for v in "aeiou" if counts[v] > 0}
#
# print(vowel_breakdown("Hello World"))
# # {'e': 1, 'o': 2}


# ################Method 9 — dict manually track each vowel
# def count_vowels(s):
#     vowel_count = {"a":0, "e":0, "i":0, "o":0, "u":0}
#     for ch in s.lower():
#         if ch in vowel_count:
#             vowel_count[ch] += 1
#     total = sum(vowel_count.values())
#     return total, vowel_count     # return both!
#
# total, breakdown = count_vowels("Hello World")
# print(total)      # 3
# print(breakdown)  # {'a':0, 'e':1, 'i':0, 'o':2, 'u':0}