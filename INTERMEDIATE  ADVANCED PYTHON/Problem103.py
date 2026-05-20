# ###########  103. Reference Leak Through Function
# Write a function that:
# Accepts a list in param
# modifies it inside function
# Then rewrite your code it so the original list stays unchanged
def safe_function(input_list):
    copied_list = input_list.copy()
    copied_list.append("safe")
    return copied_list

my_list = [1, 2, 3]
new_list = safe_function(my_list)
print(f"{"Original List : ", my_list}")
print(f"{"New List : ", new_list}")

######### Both result will be changed
# def leak_function(input_list):
#     # Modifies the original list directly
#     input_list.append("leaked")
#     return input_list
#
# # Original list
# my_list = [1, 2, 3]
# result = leak_function(my_list)
# # Result: [1, 2, 3, 'leaked']
# # my_list is now ALSO [1, 2, 3, 'leaked']
