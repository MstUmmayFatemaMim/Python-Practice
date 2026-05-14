#Find the key with the highest value.

age={"Ali":78, "Mim":203, "Mimi":98}
res=list(age.items()) #convert List
# print(res) #Print values and keys
max_value=res[0]
i=1
while i<len(res):
    #Compare only the age (index 0) like Mimi
    # if res[i] > max_value:
    #     max_value=res[i]
    # Compare only the age (index 1) like 203
    if res[i][1] > max_value[1]:
        max_value = res[i]
    i+=1
print(max_value)