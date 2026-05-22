# ################    8. Class methods & static methods //Create a Temperature class. Add a static
# ####### method celsius_to_fahrenheit(c). Add a class method from_celsius(cls, c) that returns a Temperature object.
#
class Temperature:

    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    @classmethod
    def from_celsius(cls, c):
        return cls(c)


# way 1 — use static method directly, no object needed
print("\nStaticMethod")
print(Temperature.celsius_to_fahrenheit(100))    # 212.0

# way 2 — use class method to create object first, then convert
print("\nClassMethod")
t = Temperature.from_celsius(100)                # creates object
print(Temperature.celsius_to_fahrenheit(t.celsius))  # 212.0

###########  User Define
# class Temperature:
#
#     def __init__(self, celsius):
#         self.celsius = celsius            # store celsius in object
#
#     @staticmethod
#     def celsius_to_fahrenheit(c):        # no self, no cls — pure formula
#         return (c * 9/5) + 32
#
#     @classmethod
#     def from_celsius(cls, c):            # cls = Temperature class
#         if c < -273.15:                  # absolute zero check
#             raise ValueError("Too cold! Below absolute zero.")
#         return cls(c)                    # builds and returns Temperature object
#
#
# # ── user input ──────────────────────────────
# c = float(input("Enter celsius : "))
#
# try:
#     # @classmethod creates the object
#     t = Temperature.from_celsius(c)
#
#     # @staticmethod converts the value
#     f = Temperature.celsius_to_fahrenheit(t.celsius)
#
#     print(f"\n{t.celsius}°C  =  {f}°F")
#
# except ValueError as e:
#     print(f"Error → {e}")