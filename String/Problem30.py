#############   Find common characters between two strings.
text="mango"
text1="guava"
c=[]
for x in text:
    if x in text1:
        c.append(x)
print("".join(c))

