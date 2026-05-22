############  Student // Create a Student class with name, age, grade attributes.
# Add a method introduce() that prints a sentence about the student.
class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print(f"{self.name} grade is {self.grade} and {self.age}years old.")

x=Student("Rahim",34,4.5)
x.introduce()