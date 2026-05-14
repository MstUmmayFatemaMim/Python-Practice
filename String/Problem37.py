#########       Convert "aaabbc" → "a3b2c1".

text = "message"
stock = {}

for letter in text:
    if letter in stock:
        stock[letter] += 1
    else:
        stock[letter] = 1

print(stock)

seen = []
result = ""

for letter in text:
    if letter not in seen:
        result += letter + str(stock[letter])  # uses YOUR stock dictionary
        seen.append(letter)

print(result)

# text = "message"
# seen = []
# result = ""
#
# for letter in text:
#     if letter not in seen:
#         result += letter + str(text.count(letter))
#         seen.append(letter)
#
# print(result)  # m1e2s2a1g1


# text = "message"
# stock = {}
#
# for letter in text:
#     if letter in stock:
#         stock[letter] += 1
#     else:
#         stock[letter] = 1
#
# print(stock)
#
# # Fix is here
# result = "".join(letter + str(stock[letter]) for letter in stock)
# print(result)