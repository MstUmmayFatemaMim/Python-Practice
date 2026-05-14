def change_name(n):
  n = n + " world" # creates new string, does NOT touch original
  return n
name = "hello"
change_name(name)
print(name)