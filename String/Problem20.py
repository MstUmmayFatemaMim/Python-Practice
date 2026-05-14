########    Remove duplicate characters while preserving order.
s="message"
seen=[]
for letter in s:
    if letter not in seen:
        seen.append(letter)
print("".join(seen))