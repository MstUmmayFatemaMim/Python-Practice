# # ########    6. Inheritance — Animal hierarchy // Create an Animal base class with speak().
# # # ######Then create Dog, Cat, and Bird subclasses that override speak() with their own sound.
# #########   Without Polymorphism
# class Animal:
#     def speak(self):        #########    overriding--> same method different class and attribute
#         pass        #### we leave it empty on purpose. Children will fill it in.
# class Dog(Animal):
#     def speak(self):        #########    overriding
#         # print("Woof!")    ####### if we write this.we can call this way x=Dog() x.speak().it will print properly
#         return "woof!"
#     def eat(self):
#         return "eat!"
# class Cat(Animal):
#     def speak(self):        #########    overriding
#         return "meow!"
# class Bird(Animal):
#     def speak(self):        #########    overriding
#         return "chirp!"     ####### if we do not write this we can not print this way ** print(f"Dog is {x.speak()},{x.eat()}")
#
# x = Dog()
# print(f"Dog is {x.speak()},{x.eat()}")
# y = Cat()
# print(f"Cat is {y.speak()}")
# z=Bird()
# print(f"Bird is {z.speak()}")

# ########    Polymorphism
class Animal:
    def speak(self):
        pass

    def eat(self):                    # moved to parent — all animals eat
        return "eating..."            # default behaviour


class Dog(Animal):
    def speak(self):
        return "Woof!"

    def eat(self):                    # Dog overrides with specific version
        return "eating bones!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Bird(Animal):
    def speak(self):
        return "Chirp!"


# Individual calls (what you had before)
x = Dog()
print(f"Dog is {x.speak()}, {x.eat()}")   # Dog is Woof!, eating bones!

y = Cat()
print(f"Cat is {y.speak()}")              # Cat is Meow!

z = Bird()
print(f"Bird is {z.speak()}")             # Bird is Chirp!

# Polymorphism — added now
print("\n--- Polymorphism ---")
animals = [Dog(), Cat(), Bird()]
for animal in animals:
    print(f"{animal.speak()} | {animal.eat()}")
#
# # Output:
# # Woof! | eating bones!
# # Meow! | eating...       ← Cat uses Animal's default eat()
# # Chirp! | eating...      ← Bird uses Animal's default eat()