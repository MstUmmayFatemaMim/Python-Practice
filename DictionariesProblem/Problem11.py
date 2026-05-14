#Check if a key exists in a dictionary.

age={"Ali":78, "Mim":203, "Mimi":98}
# if "Mim" in age:
#     print("Mim is here in dictionary")
# else:
#     print("Not in here")
         ########### FOUND
found=False
for x in age:
    if x=="Mim":
        found=True
        break;
if found:
    print("Mim is here in dictionary")
else:
    print("Not in here")
