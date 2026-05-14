# #######Write a function that returns factorial of a number.
def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(f"The factorial of 5 is: {factorial(5)}")


# ##########Method 2 — Recursion — classic approach
# def factorial(n):
#     if n < 0:
#         return "undefined"
#     if n == 0 or n == 1:     # base case — stops recursion
#         return 1
#     return n * factorial(n - 1)   # recursive call
# print(factorial(5))   # 120


###########33Method 3 — math.factorial — built-in best way
# import math
#
# def factorial(n):
#     if n < 0:
#         return "undefined"
#     return math.factorial(n)
#
# print(factorial(5))     # 120
# print(factorial(10))    # 3628800
# print(factorial(100))   # huge number — handles it perfectly!


# #############Method 4 — while loop
# def factorial(n):
#     if n < 0:
#         return "undefined"
#     result = 1
#     while n > 1:
#         result *= n    # multiply from n down to 2
#         n -= 1
#     return result
# print(factorial(5))   # 120

# #########Method 5 — reduce() — functional style
# from functools import reduce
# def factorial(n):
#     if n < 0:
#         return "undefined"
#     if n == 0:
#         return 1
#     return reduce(lambda acc, i: acc * i, range(1, n + 1))  ########reduce() applies the multiply operation left to right across the whole range.
#                 # How it works:
#                 # reduce(lambda acc,i: acc*i, [1,2,3,4,5])
#                 # Step 1: acc=1, i=1  → 1×1  = 1
#                 # Step 2: acc=1, i=2  → 1×2  = 2
#                 # Step 3: acc=2, i=3  → 2×3  = 6
#                 # Step 4: acc=6, i=4  → 6×4  = 24
#                 # Step 5: acc=24,i=5  → 24×5 = 120
# print(factorial(5))   # 120

########Method 6 — recursion with memoization — fastest for repeated calls
# from functools import lru_cache
# @lru_cache(maxsize=None)    # cache ALL results
# def factorial(n):
#     if n < 0:
#         return "undefined"
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
#         # How cache works:
#         # First call:  factorial(5)
#         #   → computes 1,2,6,24,120 → stores all in cache
#         #
#         # Second call: factorial(10)
#         #   → needs factorial(5) → already in cache!
#         #   → only computes 720, 5040, 40320, 362880, 3628800
#         #
#         # Third call:  factorial(5)
#         #   → instantly returns 120 from cache!
#         #   → zero computation!
# print(factorial(5))    # 120  ← computed fresh
# print(factorial(10))   # 3628800 ← reuses factorial(5)!
# print(factorial(5))    # 120  ← instant! from cache

# ######Method 7 — one liner with math.prod
# import math
# def factorial(n):
#     if n < 0:
#         return "undefined"
#     return math.prod(range(1, n + 1))   # multiply all numbers 1 to n
#             # How it works:
#             # math.prod([1, 2, 3, 4, 5])
#             # → multiplies ALL items in the iterable
#             # → 1 × 2 × 3 × 4 × 5 = 120
# print(factorial(5))   # 120

# #######Method 8 — tail recursion style
# def factorial(n, accumulator=1):
#     if n < 0:
#         return "undefined"
#     if n == 0 or n == 1:
#         return accumulator       # return result directly — no waiting!
#     return factorial(n - 1, accumulator * n)   # carry result forward
# print(factorial(5))   # 120

######Method 9 — numpy for array of factorials
# import numpy as np  #### NEED TO INSTALL
# from math import factorial as f
#
# def factorial(n):
#     if n < 0:
#         return "undefined"
#     return np.prod(np.arange(1, n + 1))   # multiply array
#
# print(factorial(5))    # 120
# print(factorial(10))   # 3628800
#
# # Bonus — get factorials of multiple numbers at once:
# numbers = [1, 2, 3, 4, 5]
# results = [int(np.prod(np.arange(1, x+1))) for x in numbers]
# print(results)   # [1, 2, 6, 24, 120]


# How it works:
# np.arange(1, 6) → array([1, 2, 3, 4, 5])
# np.prod(...)    → 1×2×3×4×5 = 120