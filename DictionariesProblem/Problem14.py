keys = ["Ali", "Mim", "Mimi"]
values = [78, 203, 98]

new_dict = {}

# We loop through the range of the length of the list (0, 1, 2)
for i in range(len(keys)):
    new_dict[keys[i]] = values[i]

print(new_dict)