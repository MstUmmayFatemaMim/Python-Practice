####Replace all spaces in a string with _.
# mess="I do my best"
# text=mess.replace(' ','_')
# print(text)

text = "Hello World From Python"
new_text = ""

for char in text:
    if char == " ":
        new_text += "_"
    else:
        new_text += char  ###Continue other word or charector
print(new_text)
