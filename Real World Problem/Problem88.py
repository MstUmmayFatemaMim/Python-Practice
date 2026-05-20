#########       Count word frequency in a paragraph.
message=("The quiet night fell over the city, bringing a quiet calm to the bustling streets. "
         "As the night grew darker, the city lights began to twinkle against the sky. It "
         "was a perfectly quiet night in the heart of the city that never truly sleeps.")


word=message.split()
stock={}
for letter in word:
    if letter in stock:
        stock[letter]+=1
    else:
        stock[letter] = 1
print(stock)

