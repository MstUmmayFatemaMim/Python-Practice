###########     Count the frequency of each word in a paragraph.
text=("The quiet morning felt so quiet and calm, offering a much-needed quiet escape from the bustling city. I decided to walk along the walkway, a familiar walk .I take every single day. The soft light created a soft atmosphere, making everything look incredibly soft and peaceful.")
word=text.split()
stock={}
for letter in word:
    if letter in stock:
        stock[letter]+=1
    else:
        stock[letter] = 1
print(stock)