# Count how many times a value appears in a list.
newlist5 = [50, 30, 70, 190, 500, 200, 50, 30]
seen=[]
for x in newlist5:
    if x not in seen:
        count=0
        for y in newlist5:
            if x == y:
                count+=1
        print(f"The count of {x} is {count}")
        seen.append(x)

        