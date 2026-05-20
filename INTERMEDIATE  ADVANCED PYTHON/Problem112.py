#  ##############112. Function That Returns Different Results Each Time
# # Write a function that:
# # Returns an incrementing number
# # Without using global variables
# # (Hint: default arguments or closures)


def number_machine():
    count = 1
    while True:
        # Hands you the current count and freezes the function right here
        yield count
        # When called again, it unpauses right here and adds 1
        count += 1

# --- How to Use It ---
# 1. Start the machine
machine = number_machine()

# 2. Use the built-in next() function to get the next number
print(next(machine))  # Output: 1
print(next(machine))  # Output: 2
print(next(machine))  # Output: 3


# def make_incrementer(start=1):
#     # This variable is locked inside the outer function's scope
#     count = start
#
#     def increment():
#         nonlocal count  # Tells Python to use the count variable from the outer scope
#         current = count
#         count += 1
#         return current
#
#     return increment
#
#
# # --- Test Case ---
# counter = make_incrementer()
#
# print(counter())  # Output: 1
# print(counter())  # Output: 2
# print(counter())  # Output: 3
