########## Reverse each word in a sentence.

# sen = "Hello World From Python"
# i=len(sen)-1
# while i>=0:
#     # print("".join(sen[i]),end="")
#     print(sen[i],end="")
#     i-=1

# sen = "Hello World From Python"
# i=0
# while i<len(sen):
#     i=len(sen)-1
#     while i>=0:
#         print(sen[i],end="")
#     i-=1
#     break
# i+=1

sen = "Hello World From Python"
words = sen.split()
print(words)
i = len(words) - 1

while i >= 0:
    while i < len(words):
        print(words[i], end=" ")
        i += 1
        break  # Stops the inner loop instantly after printing one word
    i -= 2  # Offsets the i += 1 to step backward correctly
print()

# START: i = 3
#
# ════════════════════════════════
# OUTER LOOP — Check: i >= 0?
# ════════════════════════════════
#
# ROUND 1:
# ─────────────────────────────
# i = 3 → 3 >= 0? YES → ঢোকো
#
#   INNER LOOP — Check: i < 4?
#   3 < 4? YES → ঢোকো
#     → print words[3] → "Python "
#     → i += 1 → i = 4
#     → break  → inner loop বন্ধ!
#
#   i -= 2 → i = 4 - 2 = 2
#
# ROUND 2:
# ─────────────────────────────
# i = 2 → 2 >= 0? YES → ঢোকো
#
#   INNER LOOP — Check: i < 4?
#   2 < 4? YES → ঢোকো
#     → print words[2] → "From "
#     → i += 1 → i = 3
#     → break  → inner loop বন্ধ!
#
#   i -= 2 → i = 3 - 2 = 1
#
# ROUND 3:
# ─────────────────────────────
# i = 1 → 1 >= 0? YES → ঢোকো
#
#   INNER LOOP — Check: i < 4?
#   1 < 4? YES → ঢোকো
#     → print words[1] → "World "
#     → i += 1 → i = 2
#     → break  → inner loop বন্ধ!
#
#   i -= 2 → i = 2 - 2 = 0
#
# ROUND 4:
# ─────────────────────────────
# i = 0 → 0 >= 0? YES → ঢোকো
#
#   INNER LOOP — Check: i < 4?
#   0 < 4? YES → ঢোকো
#     → print words[0] → "Hello "
#     → i += 1 → i = 1
#     → break  → inner loop বন্ধ!
#
#   i -= 2 → i = 1 - 2 = -1
#
# ROUND 5:
# ─────────────────────────────
# i = -1 → -1 >= 0? NO → বন্ধ!
# ════════════════════════════════
#
# Final Output: Python From World Hello