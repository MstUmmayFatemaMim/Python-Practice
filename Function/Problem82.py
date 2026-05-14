###########Write a function that checks if a number is prime.

def primecheck(x):
    if x < 2:
        return "Not Prime"
    for i in range(2, x):
        if x % i == 0:
            return "Not Prime"

    return "Prime"
print(f"The number is {primecheck(11)}")


# #######Method 1 — Basic for loop
# def is_prime(n):
#     if n < 2:
#         return False           # 0 and 1 are NOT prime
#     for i in range(2, n):     # check every number from 2 to n-1
#         if n % i == 0:
#             return False       # found a divisor — not prime!
#     return True                # no divisor found — prime!
#
# print(is_prime(7))    # True
# print(is_prime(10))   # False
# print(is_prime(1))    # False

# ###########Method 2 — Square root optimisation — most important trick
# import math
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):  # only up to root n
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(97))    # True
# print(is_prime(100))   # False

# ###############Method 3 — Skip even numbers — 2x faster
# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True        # 2 is the only even prime
#     if n % 2 == 0:
#         return False       # all other even numbers — not prime
#     for i in range(3, int(n**0.5) + 1, 2):  # step=2 → odd only
#         if n % i == 0:
#             return False
#     return True
#                 # How it works:
#                 # All even numbers > 2 are NOT prime (divisible by 2)
#                 # So skip ALL even numbers in the loop:
#                 #
#                 # range(3, √n+1, 2) → 3, 5, 7, 9, 11, 13...
#                 #                              ↑
#                 #                         step=2 skips evens
#                 #
#                 # For n=100:
#                 #   Method 2: checks 2,3,4,5,6,7,8,9,10  → 9 checks
#                 #   Method 3: checks 3,5,7,9             → 4 checks
# print(is_prime(17))   # True
# print(is_prime(18))   # False

# ##########Method 5 — all() with generator — one liner
# def is_prime(n):
#     if n < 2:
#         return False
#     return all(n % i != 0 for i in range(2, int(n**0.5) + 1))     ######all() short-circuits — stops as soon as it finds a divisor.
# print(is_prime(13))   # True
# print(is_prime(15))   # False

# ############Method 6 — any() opposite approach
# def is_prime(n):
#     if n < 2:
#         return False
#     return not any(n % i == 0 for i in range(2, int(n**0.5) + 1))       #####Opposite logic of all() — not any(divisor exists) = prime.
#
# print(is_prime(11))   # True
# print(is_prime(12))   # False

# #############Method 9 — functools.reduce — functional style
# from functools import reduce
#
# def is_prime(n):
#     if n < 2:
#         return False
#     return reduce(
#         lambda acc, i: acc and n % i != 0,
#         range(2, int(n**0.5) + 1),
#         True        # starting value
#     )
#             # reduce applies lambda left to right:
#             #   start: acc = True
#             #   i=2: True  and 23%2≠0 → True  and True  → True
#             #   i=3: True  and 23%3≠0 → True  and True  → True
#             #   i=4: True  and 23%4≠0 → True  and True  → True
#             #   ...
#             #   final: True → prime!
#             #
#             # For n=25, i=5:
#             #   True and 25%5≠0 → True and False → False → not prime
# print(is_prime(23))   # True
# print(is_prime(25))   # False

# ##########Method 7 — sympy library — production ready
# from sympy import isprime       ###### NEED TO INSTALL
#
# print(isprime(17))           # True
# print(isprime(100))          # False
# print(isprime(982451653))    # True  ← huge prime, instant!