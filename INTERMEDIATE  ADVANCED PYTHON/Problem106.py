# ##############      106. Custom Copy Function (No copy Module)
# Write your own function that:
# Deep copies a list of lists
# Without using copy or deepcopy


def deep_copy_recursive(data):
    # Base case: if it is a list, recursively copy its contents
    if isinstance(data, list):
        # return [deep_copy_recursive(item) for item in data]
        # This code does the exact same thing behind the scenes:
        new_list = []
        for item in data:
            copied_item = deep_copy_recursive(item)
            new_list.append(copied_item)
        return new_list

    # If it is a primitive/immutable (int, string, float), return it directly
    return data

# --- Test Case ---
original = [[1, 2], [3, 4]]
cloned = deep_copy_recursive(original)

# Modify the clone to prove separation
cloned[0][0] = 99

print("Original:", original)  # Output: [[1, 2], [3, 4]] -> Untouched!
print("Cloned:  ", cloned)  # Output: [[99, 2], [3, 4]]
