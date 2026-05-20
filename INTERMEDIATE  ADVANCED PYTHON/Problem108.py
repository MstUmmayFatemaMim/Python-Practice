# ###########        108. Method Side Effects
# Write a function that:
# Sorts a list
# Returns the sorted list
# But does NOT modify the original


def safe_sort(input_list):
    # Generates a new sorted list, leaving the original completely untouched
    return sorted(input_list)

# --- Test Case ---
original_list = [5, 2, 9, 1]
sorted_result = safe_sort(original_list)

print("Original List:", original_list)  # Output: [5, 2, 9, 1] (Unchanged!)
print("Sorted Result:", sorted_result)  # Output: [1, 2, 5, 9]
