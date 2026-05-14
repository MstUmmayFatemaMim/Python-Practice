#Sort a dictionary by values.
age={"Ali":78, "Mim":203, "Mimi":98}
res=list(age.items()) #convert List
for x in sorted(res, key=lambda x: x[1]):
    print(x)