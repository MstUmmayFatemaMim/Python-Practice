###########     Write a function that modifies a string without changing the original.
def mfunction(oldtext,extratext):
    newtext = oldtext+extratext
    return newtext

o="Hello"
p=mfunction(o,"mim")
print(p)
print(o)
