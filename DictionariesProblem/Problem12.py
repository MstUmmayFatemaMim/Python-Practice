#Sort a dictionary by keys.

age={"Alibaba":78, "Mimua":203, "Mimi":98}
res=list(age.items()) #convert List
# print(res) #Print values and keys
# max_value=res[0]
# i=1
# while i<len(res):
#     #Compare only the age (index 0) like Mimi
#     # if res[i] > max_value:
#     #     max_value=res[i]
#     for x in age:
#         if age[x] < len(max_value):
#             print(x)
# i+=1

        ### Sorted by A-Z
# for i in sorted(res):
#     print(i)


        ### Sorted by key length

for x in sorted(res, key=lambda x: len(x[0])):
    print(x)