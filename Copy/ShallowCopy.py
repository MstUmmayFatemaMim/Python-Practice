            ####  SHALLOW COPY --> Value different or Value same, but Location always different
Scopy=[4,5,6,8]
Scopy1=Scopy.copy()
print("Shallow Copy : ")
print(Scopy,Scopy1)
print(id(Scopy) , id(Scopy1))
Scopy1[1]=5000      #Update the value,value will change only Scopy1, location also changed
print(Scopy,Scopy1)
print(id(Scopy) , id(Scopy1))

                ####  SHALLOW COPY Nested List -->
Sncopy=[[4,5,6,8],[7,3,2,9]]
Sncopy1=Sncopy.copy()
print("Shallow Copy Nested : ")
print(f"Sncopy: {Sncopy}",f"Sncopy1: {Sncopy1}")
print(f"Sncopy: {id(Sncopy)}" , f"Sncopy1: {id(Sncopy1)}")
Sncopy1[1][0]=700   ##### Change single value but It shows both Sncopy and Sncopy1.
print("After Updating the Sncopy1:")
print(f"Sncopy: {Sncopy}",f"Sncopy1: {Sncopy1}")
print(f"Sncopy: {id(Sncopy)}" , f"Sncopy1: {id(Sncopy1)}")

Sncopy.append([34,55,63,88])    #It shows only for Sncopy. Not showing the Sncopy1
print("After Adding the Sncopy:")
print(f"Sncopy: {Sncopy}",f"Sncopy1: {Sncopy1}")
print(f"Sncopy: {id(Sncopy)}" , f"Sncopy1: {id(Sncopy1)}")
