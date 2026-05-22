##########  Explain with code why tuples are immutable but can contain mutable objects.

my_tuple = (1, 2, 3)

# ######my_tuple[0] = 99    # TypeError

my_tuple = (1, 2, [10, 20, 30])         ####### tuple is immutable but within the list is mutable.Tuple do not check this
print(my_tuple)

my_tuple[2].append(99)
print(my_tuple)

# # # Tuple is immutable means →
# # #     tuple cannot change WHICH objects it points to
# # #
# # # But the objects it points to →
# # #     can change their own contents freely!
# # #
# # # Tuple locks the DOORS not the ROOMS inside!