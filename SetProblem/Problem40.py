#########   Remove duplicate words from a sentence.
message = {"The quick brown fox jumps over the lazy dog."}
seen={}
for letter in message:
    if letter not in seen:
        seen.add(letter)
print("".join(seen))