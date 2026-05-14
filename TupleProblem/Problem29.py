mytuple = (50, 30, 70, 30, 500, 30, 60)
max=mytuple[0] #assume max value
min=mytuple[0] #assume min value

#work for max value
for x in mytuple:
    if x> max:
        max=x
print(max)

#work for min value
for x in mytuple:
    if x < min:
        min = x
print(min)
