# student = {
#     "names" : "Mim",
#     "marks" : 89
# }
#
# student = {
#     "names" : "Mimi",
#     "age" : 1
# }
# ######give same dic name but  value change .Output True.
# print(student == student)
# print(id(student) == id(student))        #####Memory location different
# print(student is student)

student = {
    "names" : "Mim",
    "marks" : 89
}

person = {
    "names" : "Mim",
    "marks" : 89
}
######give same dic name but  value change .Output True.
print(student == person)                #### Value same
print(id(student) == id(person))        #####Memory location different
print(student is person)