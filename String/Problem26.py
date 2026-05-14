#########       Check if one string is a rotation of another.

s1="live"
s=list(s1)
c=[]
i=len(s)-1
s2="evil"
s3=list(s2)
while i>=0:
    c.append(s[i])
    i-=1
# print("".join(c))
if s3==c:
    print(f"S3  {s3} equal to c {c}")
else:
    print("Not equal")