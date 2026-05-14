############
# Immutable = cannot change after creation.
# A string is like a name written in stone. You can write a new stone, but you cannot erase the old one.
# In Python, you never modify a string. You always create a new one.

# Rule 1 — You cannot change a character inside a string
name = "hello"
name[0] = "H"    # ERROR!
# Python says no. The string "hello" is locked the moment it is created.

# Rule 2 — Reassigning is NOT changing
name = "hello"
name = "Hello"   # This is NOT changing the string
# What actually happens here:

# "hello" is created in memory and stays there untouched
# "Hello" is a brand new string created separately
# The variable name just moves to point at the new one
# You are not editing. You are replacing.

# Rule 3 — Methods like replace() also give you a NEW string
name = "hello"
name.replace("h", "H")   # does nothing visible
print(name)               # still "hello"
# You must save the result:
name = name.replace("h", "H")
print(name)   # "Hello"

# The simple test to understand it
name = "hello"
print(id(name))   # example: 140200

name = "Hello"
print(id(name))   # example: 140999  ← different number!
# id() gives the memory address. If the address changed, it is a different object. Python never modified the first one.

