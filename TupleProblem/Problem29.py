############        Find the maximum and minimum value in a tuple.

mytuple = (50, 30, 70, 30, 500, 30, 60)
max_val=mytuple[0] #assume max value
min_val=mytuple[0] #assume min value

# #work for max value
# for x in mytuple:
#     if x> max_val:
#         max_val=x
# print(max_val)
#
# #work for min value
# for x in mytuple:
#     if x < min_val:
#         min_val = x
# print(min_val)

for x in mytuple:
    if x > max_val:
        max_val = x
    if x < min_val:
        min_val = x

print(f"Max : {max_val}")
print(f"Min : {min_val}")

########    Using Build in max min function
print(f"Max is {max(mytuple)}")

print(f"Min is {min(mytuple)}")

output=sorted(mytuple)
print(f"Max Value is {output[0]}")
print(f"Max Value is {output[len(mytuple)-1]}")