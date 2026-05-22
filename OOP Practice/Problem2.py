####### 2. Rectangle calculator // Build a Rectangle class with width and height. Add methods
########## area() and perimeter() that return computed values.
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * self.width + self.height

x=Rectangle(10,20)
print(f"Area: {x.area()}")
print(f"Perimeter: {x.perimeter()}")
