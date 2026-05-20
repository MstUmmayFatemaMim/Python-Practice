# ########### 107. Shared Reference Detector
# Write code that:
# Detects whether two variables point to the same list
# Without using is directly

def is_shared_reference(a, b):
    # Compares the unique memory addresses of both variables
    return id(a) == id(b)

# --- Test Cases ---
list1 = [1, 2, 3]
list2 = list1        # Shared reference (points to the same list)
list3 = [1, 2, 3]    # Different list (same values, different memory)

print(is_shared_reference(list1, list2))  # Output: True
print(is_shared_reference(list1, list3))  # Output: False
