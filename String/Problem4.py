################Convert a string to uppercase without using .upper().
s = "hello world"
result = ""

for char in s:
    if 'a' <= char <= 'z':          # check if lowercase
        result += chr(ord(char) - 32)  # shift ASCII by 32
    else:
        result += char              # keep space/symbols as-is

print(result)   # HELLO WORLD