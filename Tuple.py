# thistuple = ("apple",)
# print(type(thistuple))
#
# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))
# tuple1 = ("abc", 34, True, 40, "male")
# print(tuple1)
# print(type(tuple1))
# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple)

# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#
# (*yellow,) = fruits
#
# # print(green)
# print(yellow)
# # print(red)
# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)