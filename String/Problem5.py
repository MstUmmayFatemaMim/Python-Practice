##############Convert a string to lowercase without using .lower().
s = "Hello World"
result = ""

for char in s:
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)  # shift ASCII by 32
    else:
        result += char

print(result)