#Convert json to Python
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y)
#Convert Python to JSON
# import json
# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# convert into JSON:
# y = json.dumps(x)

# the result is a JSON string:
# print(y)

# import json
#
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
#
# print(json.dumps(x))

# indent — সুন্দর করে দেখাও
import json

x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)    # ← এটা না করলে indent কাজ করবে না!

# print(json.dumps(y, indent=4))
print(json.dumps(y, indent=4, separators=(". ", ":") ) )#indent use for gap and separtors use for ., =/ to organize the nice view.It can create the view easily

# output:
# {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }