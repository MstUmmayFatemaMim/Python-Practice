#############Write a function that sorts a list without using .sort().

mylist = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(mylist)
for i in range(n-1):
  for j in range(n-i-1):
# Why n-i-1?
# After each pass i, the last i elements
# are already sorted — no need to check them!
# Pass 0 (i=0): range(8-0-1) = range(7) → j=0,1,2,3,4,5,6
# Pass 1 (i=1): range(8-1-1) = range(6) → j=0,1,2,3,4,5
# Pass 2 (i=2): range(8-2-1) = range(5) → j=0,1,2,3,4
# ...keeps shrinking!
#
# [64,34,25,12,22,11,90,5, | 5,11,22...]
#                           ↑
#                     already sorted zone (don't touch!)
    if mylist[j] > mylist[j+1]:         #check the value
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]       #swap the value

print(mylist)