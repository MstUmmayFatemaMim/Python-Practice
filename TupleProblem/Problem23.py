# tuple1=(1,2,5,4,5,1,7,2,9) #touple e value assign
mytuple = (50, 30, 70, 30, 500, 30, 60)

for x in mytuple:      #take every value
    count = 0
    for y in mytuple:    # take full touple
        if y == x:
            count = count + 1
    print(f"{x} have {count} times")