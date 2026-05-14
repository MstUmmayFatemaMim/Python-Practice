############Write a function that finds common elements between two lists.

def similar_checker(a,b):
    c=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                c.append(a[i])
    return c

a=[2,4,6,21,9,3,7]
b=[3,6,2,7,9,5,4]
print(similar_checker(a,b))
