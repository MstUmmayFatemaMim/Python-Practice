# #######      104. Identity vs Equality Debugger
# Write a function compare(a, b) that prints:
# "same object" if a is b
# "same value" if a == b
# "different" otherwise
# Test with:
# lists
# tuples
# integers

def compare(a, b):
    if a is b:
        print("same object")
    elif a == b:
        print("same value")
    else:
        print("different")


# 1. LISTS (Mutable)
l1 = [1, 2]
l2 = [1, 2]
compare(l1, l2)       # Prints: "same value" (Different memory locations, same data)


# 2. INTEGERS (Small Integer Caching)
compare(10, 10)       # Prints: "same object"
compare(999, 999)     # Prints: "same object" (In modern Python/CPython REPL)

# 3. TUPLES (Immutable)
t1 = (1, 2)
t2 = (1, 2)
compare(t1, t2)       # Prints: "same object" (Python optimizes immutable literal duplicates)
