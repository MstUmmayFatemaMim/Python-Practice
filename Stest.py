        # Create a list of numbers from 1 to 10 and print only the even numbers.
# newlist=[]
# i=1
# while i<=10:
#     if i%2==0:
#         newlist.append(i)
#     i=i+1
# print(newlist)

# Write a function that returns the sum of all elements in a list.
# s=0;
# def add(a):
#     return s+a
# newlist1=[10,20,30,40,50]
# for x in newlist1:
#     sum=add(newlist1)
# print(sum)
# s = 0
#
# def add(s, a):      # ✅ s কে parameter হিসেবে নাও
#     return s + a    # ✅ number + number = সঠিক!
#
# newlist1 = [10, 20, 30, 40, 50]
#
# for x in newlist1:
#     s = add(s, x)   # ✅ x পাঠাও (list না!)
#                     # ✅ s update করো!
#                     # ✅ sum নাম ব্যবহার করো না
#
# print(s)
# # → 150 ✅
# def add(a):
#     s = 0;
#     for x in a:
#         s += x
#     return s
# newlist1=[10,20,30,40,50]
# print(add(newlist1))

# Reverse a list without using .reverse() or slicing.
#
# newlist2=[10,20,30,40,50]
# newlist3=[]
# i=len(newlist2)-1
# while i>=0:
#     newlist3.append(newlist2[i])
#     i=i-1
# print(newlist3)

        # Reverse a list without using .reverse() or slicing.
# newlist4=[50,30,70,190,500,200]
# listmax = newlist4[0]
# for i in range(len(newlist4)):
#     if newlist4[i]>=listmax:
#         listmax=newlist4[i]
# print(listmax)


# Remove all duplicate values from a list.
# newlist5=[50,30,70,190,500,200,50,30]
# newlist5.sort()
# # print(newlist4)
# i=0
# while i<len(newlist5)-1:
#     if(newlist5[i+1]==newlist5[i]):
#         newlist5.pop(i+1)
#     i=i+1
# print(newlist5)

# age = 14
# is_student = False
# has_discount_code = True
#
# if (age < 18 or age > 65) and not is_student or has_discount_code:
#   print("Discount applies!")

# username = "Tobias"
# password = "secret123"
# is_verified = False
#
# if username and password and not is_verified:
#   print("Login successful")
# else:
#   print("Login failed")

# temperature = 12
# is_sunny = True
#
# if temperature > 20:
#   if is_sunny:
#     print("Perfect beach weather!")
# else:
#     print("Not Perfect beach weather!")

# def my_function(fname):
#   print(fname + " Refsnes")
#
# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# def my_function(name): # name is a parameter
#   print("Hello", name)
#
# my_function("Emil") # "Emil" is an argument
#
# def my_function(animal, name):
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)
# my_function("Buddy","dog")

# def my_function(*kids):
#     for x in kids:
#         print("The youngest child is " + x)
#
# my_function("Emil", "Tobias", "Linus","Mim","Saqib","Sajid")

# def myfunc1():
#   x = "Jane"
#   def myfunc2():
#     nonlocal x
#     x = "hello"
#   myfunc2()
#   return x
#
# print(myfunc1())

# def factorial(n):
#   # Base case
#   if n == 0 or n == 1:
#     return 1
#   # Recursive case
#   else:
#     return n * factorial(n - 1)
#
# print(factorial(5))

# def fibonacci(n):
#   if n <= 1:
#     return n
#   else:
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# print(fibonacci(7))

# def sum_list(numbers):
#   if len(numbers) == 0:
#     return 0
#   else:
#     return numbers[0] + sum_list(numbers[1:])
#
# my_list = [1, 2, 3, 4, 5]
# print(sum_list(my_list))

# def my_generator():
#   yield 1
#   yield 6
#   yield 3
#
# for value in my_generator():
#   print(value)
# def fibonacci():
#   a, b = 0, 1
#   while True:
#     yield a
#     a, b = b, a + b
#
# # Get first 100 Fibonacci numbers
# gen = fibonacci()
# for _ in range(100):
#   print(next(gen))

# Tuple থেকে iterator বানাও
# mytuple = ("apple", "banana", "cherry")
# 
# myit = iter(mytuple)        # iterator বানালাম
# # print(myit)
# print(next(myit))           # output: apple
# # print(next(myit))           # output: banana
# # print(next(myit))           # output: cherry
# # print(next(myit))           # 💥 StopIteration! আর নেই

# import mymodule
#
# x=dir(mymodule)
# print(x)

# import datetime
# x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.month)
# print(x.day)
# print(x.strftime("%A"))
# print(x.strftime("%d"))
# print(x.strftime("%y"))
# x1 = datetime.datetime(2018, 6, 1)
#
# print(x1.strftime("%B"))
# print(x1.strftime("%d"))
# print(x1.strftime("%A"))

# import json
# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# # parse x:
# y = json.loads(x)
# # the result is a Python dictionary:
# print(y)

# import json
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# print(json.dumps(x))

# import camelcase
#
# c = camelcase.CamelCase()
#
# txt = "lorem ipsum dolor sit amet"
# x=c.txt
# print(x)

def myfunc():
  x = 5

x = myfunc()
print(x)