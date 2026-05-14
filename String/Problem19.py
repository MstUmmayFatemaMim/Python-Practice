##########  Capitalize the first letter of each word.
text = "hello world from python"
#
# txt=text.title()      #######     Build in method
# print(txt)

text1=text.split()
print(text1)
text2=[]
for word in text1:
    new_word = word[0].upper() + word[1:].lower()   ##### first character will be upper and except first letter it will print the other letter lower
    text2.append(new_word)
print(text2)
