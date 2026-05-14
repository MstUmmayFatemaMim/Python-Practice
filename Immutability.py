#Immutability Object:A immutable object is an object that can have its value modified in different placed.
#Objects, reassigning a variable does not affect others previously pointing to the same value, as a new object
#is created for the updated variable.Example:integers, floats, booleans, strings, and tuples

#Immutable: Seperate-->Changes are not shared
#Integers
num=10
print(id(num)) # OUTPUT 140712252024008

num+=1
print(id(num)) #OUTPUT 140712252024040

a=5
b=a
print(a,b)
print(id(a),id(b))
b+=1    #Change the value,the memory address will be change
print(b)
print(id(b))
#OUTPUT
# 5 5
# 140712204248104 140712204248104
# 6
# 140712204248136



#Tuples
coords=(100,200)
#coords[0]=150   #'tuple' object does not support item assignment
print(id(coords))  #OUTPUT 2031725002368
print(coords)
