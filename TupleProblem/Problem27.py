mytup = ("apple", "lichi", "graps", "orange")
mytuple = list(mytup)
temp=mytuple[0]
mytuple[0]=mytuple[len(mytuple)-1]
mytuple[len(mytuple)-1]=temp
mytup=tuple(mytuple)
print(mytup)

