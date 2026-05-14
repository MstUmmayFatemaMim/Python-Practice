# ##########      Remove punctuation from a string.

text = "Hello, world ! from ; Python?"
new_text = ""
for char in text:
    # if char in "!#$%&'()*+,-./:;<=>?@[\]^_{|}~` ":        #########   Not working for single slash
    # if char in r"!#$%&'()*+,-./:;<=>?@[\]^_{|}~` ":       ########    ****     Works Properly
    if char in "!#$%&'()*+,-./:;<=>?@[\\]^_{|}~` ":
        new_text += " "
    else:
        new_text += char
print(new_text)

# #########       Build in function
# import string
# text = "Hello, World! This is a test... baseline string."
#
# # Create a translation table that maps all punctuation to None
# translator = str.maketrans("", "", string.punctuation)
#
# # Remove the punctuation
# clean_text = text.translate(translator)
#
# print(clean_text)   # Output: Hello World This is a test baseline string

