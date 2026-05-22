# Write a function that returns the sum of all elements in a list.
#
# s=0
# def add(s, a):
#     return s + a
#
# newlist1 = [10, 20, 30, 40, 50]
# for x in newlist1:
#     s = add(s, x)
# print(s)

def add(a):
    s = 0;
    for x in a:
        s += x
    return s
newlist1=[10,20,30,40,50]
print(add(newlist1))