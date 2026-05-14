#Mutable Object:A mutable object is an object that can have its value modified in-placed.Example:lists, dictionaries, and sets
#Mutable: Linked -->Changes are shared

#LISTS
grades=[16,8,12]
print("Grades : ")
print(id(grades))
grades[0]=20
print(id(grades))
grades.append(20)
print(id(grades))
#SETS
x={1,2,3}
y=x
print("SETS : ")
print(x,y)
print(id(x),id(y))
y.add(13)
print(x,y)
print(id(x),id(y))
# {1, 2, 3} {1, 2, 3}
# 2233879921824 2233879921824
# {1, 2, 3, 13} {1, 2, 3, 13}
# 2233879921824 2233879921824

x={1,2,3}
y=x.copy() #It forces Python to create a completely new object in memory.Memory address will be different.
# The copy does not affect the original, it does not guarantee that nested mutable objects are fully independent
print("Shallow Copy Example with SETS: ")
print(x,y)
print(id(x),id(y))
y.add(13)
print(x,y)
print(id(x),id(y))

#Dictuionaries:
products = {"milk":2.29,
            "egg":1.79,
            "banana":0.99}
print(products)
print(id(products))
products["bread"]=1.29
print(products)
print(id(products))

# a=[1,[2,3]]
# b=a.copy()
# print(a)
# print(id(a))
# print(b)
# print(id(b))
# b[1][0]=9
# print(b)
# print(id(b))
# print(a)
# print(id(a))
