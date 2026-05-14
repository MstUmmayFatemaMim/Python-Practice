# #Write code where modifying one list affects another.
            ####Assignment
# a = [1, 2, 3]
# b = a            # b points to same list
# b.append(4)
# print(a)  # [1, 2, 3, 4]  ← a changed!
# print(b)  # [1, 2, 3, 4]
                ########Shallow copy with nested list
# a = [1, 2, 3]
# b = a            # b points to same list
# b.append(4)
# print(a)  # [1, 2, 3, 4]  ← a changed!
# print(b)  # [1, 2, 3, 4]

            ###### List passed into a function
# def add_item(lst):
#     lst.append(99)      # modifies the original list!
# a = [1, 2, 3]
# add_item(a)
# print(a)  # [1, 2, 3, 99]  ← a changed outside the function!

                    #######List inside a dictionary
# data = {"scores": [10, 20, 30]}
# backup = data            # same dict, same inner list
# backup["scores"].append(99)
# print(data["scores"])    # [10, 20, 30, 99]  ← changed!

                        ##########Multiple variables from same list (slice trick trap)
# a = [1, 2, 3, 4, 5]
# b = a[1:3]       # looks like a new list...
# a[1] = 99        # modify a directly
# print(a)  # [1, 99, 3, 4, 5]
# print(b)  # [2, 3]  ← b did NOT change here
# # BUT with numpy arrays it DOES affect:
# import numpy as np                                ############Need to install numpy
# a = np.array([1, 2, 3, 4, 5])
# b = a[1:3]       # numpy slice = shared memory!
# a[1] = 99
# print(b)  # [99, 3]  ← b changed!


# #Write code where modifying one tuple affects another.
# a = (1, 2, 3, 4)
# b = a             # Initially b points to a
#
# # 1. Convert to list to allow modification
# temp_list = list(a)
# temp_list.append(5)
#
# # 2. Convert back to tuple and update BOTH variables
# a = tuple(temp_list)
# b = a
# print(a,b)
# print(id(a),id(b))

# # # #Write code where modifying set affects another.
# a={1,2,3,4}    #create variable
# b=a         #assign in b or reference deya
# print(a,b)
# print(id(a),id(b))
# a.add(333)
# print(a,b)
# print(id(a),id(b))


# # # #Write code where modifying one dictionary affects another.
# # ## Assign the value
student = {
    "name":"Mim",
    "age":24
}
person=student      ##assign value does not change the memory location
print(student,person)
print(id(student),id(person))
person["address"]="Dhaka"
print(person,student)
print(id(student),id(person))

