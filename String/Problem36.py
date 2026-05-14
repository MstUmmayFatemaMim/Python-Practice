############        Convert a string like "a2b3" → "aabbb".
result = "a2b3"
decoded = ""

i = 0
while i < len(result):
    letter = result[i]        # letter
    count = int(result[i+1])  # number next to it
    decoded += letter * count # repeat letter by count
    i += 2                    # jump 2 steps (letter + number)

print(decoded)