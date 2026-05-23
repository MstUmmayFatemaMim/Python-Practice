########    Check if one set is a subset of another.

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

print(f"Way 1 : {x.issubset(y)}")

print(f"Way 2 : {x<=y}")