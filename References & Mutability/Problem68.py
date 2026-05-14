######Demonstrate is vs == using integers.

# a=10
# b=a
# print(id(a),id(b))
# print(a==b)
# print(b is a)

###########Method 1 — small integers is and == both True
# a = 10
# b = 10          # both point to cached object
#
# print(a == b)   # True  ✅ same value
# print(a is b)   # True  ✅ same cached object
# print(id(a) == id(b))  # True — same address
# ####310 is inside the cache range (-5 to 256) so Python reuses the same object. Both a and b point to the exact same integer object.

# ############Method 2 — large integers == True but is False
# a = 1000
# b = 1000        # outside cache — two new objects
#
# print(a == b)   # True  ✅ same value
# print(a is b)   # False ❌ different objects
# print(id(a) == id(b))  # False — different addresses
# #############1000 is outside the cache range so Python creates a fresh integer object each time. Same value, different identity.
#
# ###########3Method 3 — negative integers boundary
# a = -5
# b = -5
# print(a is b)   # True  ✅ -5 is cached
#
# a = -6
# b = -6
# print(a is b)   # True -6 is cached
# ######Cache starts at -5. Anything below that is a new object every time.
#
# ##########Method 4 — boundary at 256 and 257
# a = 256
# b = 256
# print(a == b)   # True  ✅
# print(a is b)   # True  ✅ 256 is last cached number
#
# a = 257
# b = 257
# print(a == b)   # True  ✅
# print(a is b)   # False ❌ 257 is first uncached number
# ##########3256 is the exact boundary. This is a famous Python interview question!
#
# ############Method 5 — assignment always is True
# a = 1000        # large number outside cache
# b = a           # b points to same object as a
#
# print(a == b)   # True  ✅
# print(a is b)   # True  ✅ — because b = a, not b = 1000
# ##########When you do b = a, b gets the same reference as a — regardless of the value. So is is always True for direct assignment.
#
# ##########Method 6 — arithmetic result comparison
# a = 5 + 5      # result: 10 — inside cache
# b = 10
#
# print(a == b)   # True  ✅
# print(a is b)   # True  ✅ — 10 is cached
#
# a = 500 + 500   # result: 1000 — outside cache
# b = 1000
#
# print(a == b)   # True  ✅
# print(a is b)   # False ❌ — 1000 not cached
# ###########The result of arithmetic is also subject to the same caching rules — inside range reuses cached object, outside range creates new one.
#
# #########Method 7 — different values both False
# a = 10
# b = 20
#
# print(a == b)   # False ❌ different values
# print(a is b)   # False ❌ different objects
# ###########When values differ, both == and is are False. Even though both are cached, they are cached as different objects.
#
# ##########Method 8 — prove with id() completely
# a = 10
# b = 10
# c = 1000
# d = 1000
#
# print(id(a) == id(b))   # True  — cached, same object
# print(id(c) == id(d))   # False — not cached, different
#
# print(f"id(a) = {id(a)}")
# print(f"id(b) = {id(b)}")   # same as id(a)!
# print(f"id(c) = {id(c)}")
# print(f"id(d) = {id(d)}")   # different from id(c)!
#
# ###########Method 9 — sys.intern force same object for strings (bonus)
import sys

# Python also interns short strings
# a = "hello"
# b = "hello"
# print(a is b)   # True  ✅ — Python interns short strings

# # Large integers can be forced same with assignment only
x = 99999
y = x           # y IS x
print(x is y)   # True  ✅

z = 99999       # new object
print(x is z)   # False ❌ — different object same value