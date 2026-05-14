############        Check if a string contains only alphabets.
x="123MIM"
i=0
while i<len(x):
    if x[i] not in 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM':
        print("Not Alphabets")
        break
    i+=1
else:
    print("Alphabets")