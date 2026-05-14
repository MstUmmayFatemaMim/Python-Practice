#######     Find the most frequent character in a string.

m="mimimimgog"
i=0
count={}
while i<len(m):
    char=m[i]       ##### # .lower() turns capital 'M' or 'I' into small 'm' or 'i' ****** char = m[i].lower()
    if char in count:
        count[char]+=1
    else:
        count[char]=1
    i+=1
print(count)
highcharts=max(count,key=count.get)     ## dictionary -->প্রতিটা key এর value দিয়ে তুলনা করো
print(highcharts,"=",count[highcharts])