# # ##########  7. Encapsulation — Employee salary // Build an Employee class with a private _salary.
# # ########### Use a property getter/setter so salary can't be set below 0. Raise a ValueError if attempted.
# #
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     @property
#     def salary(self):
#         return self.__salary
#
#     @salary.setter
#     def salary(self, value):
#         if value < 0:
#             raise ValueError("Salary is not valid! (Cannot be less than zero.)")
#         self.__salary = value
#
# # 1. Get user input for Name and Salary
# user_name = input("Enter employee name: ")
# user_input_salary = input("Enter employee salary: ")
#
# # 2. Process the input and catch errors
# try:
#     # Convert the text input into a whole number
#     clean_salary = int(user_input_salary)
#
#     # Try to create the employee object
#     emp = Employee(user_name, clean_salary)
#     print(f"Success! Employee {emp.name} created with a salary of {emp.salary}.")
#
# except ValueError as error:
#     # This will catch negative numbers AND text errors (like entering "abc")
#     print(f"Error: {error}")

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary        # ✅ calls the setter — validation runs here too
#                                     # NOT self.__salary = salary (that skips setter)
#
#     @property                       # step 1: marks this method as a getter
#     def salary(self):               # method name becomes the property name
#         return self.__salary        # returns the private attribute
#
#     @salary.setter                  # step 2: marks this as the setter for 'salary'
#     def salary(self, value):        # same method name, but takes a value
#         if value < 0:
#             raise ValueError("Salary cannot be negative.")
#         self.__salary = value       # only stores if validation passes
#
#
# x = Employee("Toyota", 20000)
#
# # reading salary — runs getter automatically
# print(x.salary)           # 20000
#
# # updating salary — runs setter automatically
# x.salary = 25000
# print(x.salary)           # 25000
#
# # trying invalid salary — raises ValueError
# try:
#     x.salary = -500
# except ValueError as e:
#     print(f"Error: {e}")  # Error: Salary cannot be negative.
#
# # trying invalid salary in constructor
# try:
#     y = Employee("Honda", -9999)
# except ValueError as e:
#     print(f"Error: {e}")  # Error: Salary cannot be negative.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self.__salary = value


# --- user input section ---
name   = input("Enter employee name   : ")
salary = int(input("Enter employee salary : "))

try:
    emp = Employee(name, salary)
    print(f"\nEmployee Created!")
    print(f"Name   : {emp.name}")
    print(f"Salary : {emp.salary}")

    choice = input("\nDo you want to update salary? (yes/no) : ")

    if choice == "yes" :
        new_salary = int(input("Enter new salary : "))
        emp.salary = new_salary
        print(f"\nSalary updated!")
        print(f"Name   : {emp.name}")
        print(f"Salary : {emp.salary}")

except ValueError as e:
    print(f"\nError : {e}")
#
#     # 1.self.__salary     →  double underscore = private = no outside access
#     # 2. @ property         →  reading door  →  emp.salary         → runs getter
#     # 3. @ salary.setter    →  writing door  →  emp.salary = value → runs setter
#     # 4. raise ValueError  →  if value is bad, stop and show error