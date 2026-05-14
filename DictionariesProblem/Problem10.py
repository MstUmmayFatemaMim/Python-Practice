#Reverse a dictionary (value → key).

age={"Ali":78, "Mim":203, "Mimi":98}
            ####### WAY 1
# res=list(age.items()) #convert List
# for x,y in res:
#     print(y,x)
            ########## Way  for checking
#for key in age: only work for key
# for x in age:
#     print(x)

        ####### WAY 3
# for key,value in age.items(): #key + value 2 tai thake ##unpack
#      print(value,key)
        ######## WAY 4
# for x in age.items():
#     # x = ("Ali",78), ("Mim",203), ("Mimi",98)
#     # key+value tuple! ✅
#     print(x[1],x[0])