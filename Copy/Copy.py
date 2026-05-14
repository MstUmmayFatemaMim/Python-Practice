                    #COPY
        ## "=" Copy -->same memory and same value
lst1=[1,2,5,7,3]
lst2=lst1
print(lst1)
print(id(lst1))
print(lst2)
print(id(lst2))
lst2[2]=9000
print(lst1 , lst2)
print(id(lst1) , id(lst2))



