# ###########      109. Dictionary Key Trap
# Write code that shows:
# Why a list cannot be a dictionary key
# Why a tuple can

# 1. Your original data starts as a list
my_list_key = [1, 2]

# 2. CONVERSION STEP: Turn the list into a frozen tuple
safe_tuple_key = tuple(my_list_key)

# 3. USE IT: Now it works perfectly as a dictionary key!
my_dictionary = {}
my_dictionary[safe_tuple_key] = "Successfully Stored Data!"

print(my_dictionary)
# Output: {(1, 2): 'Successfully Stored Data!'}
