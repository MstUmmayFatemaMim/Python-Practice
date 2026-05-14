#######Check if a string is a palindrome.

s1="mimim"
s=list(s1)
c=[]
i=len(s)-1
while i>=0:
    c.append(s[i])
    i-=1

if s==c:
    print("Palindrome")
else:
    print("Not Palindrome")
