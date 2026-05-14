############Fix shallow copy using copy.deepcopy().       *****the inner lists are not shared!
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)   # copies everything
b[0].append(99)
print(a)   # [[1, 2], [3, 4]]
print(id(a))    #memory address changed
print(b)   # [[1, 2, 99], [3, 4]]
print(id(b))    #memory address changed