###########     Count frequency of each character using a dictionary.
text="message"
stock={}
for letter in text:
    if letter in stock:
        stock[letter]+=1
    else:
        stock[letter] = 1
print(stock)
print("".join(stock))