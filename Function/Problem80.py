# ##########Write a function that removes duplicates from a list.
def dupfunction(newlist):

    return list(dict.fromkeys(newlist))     #### Call the function

print(dupfunction(newlist=[3,4,6,3,2,7,4,9,2,6,5,9,400]))

############    Using set-->it automatically remove the duplicate value
# def dupfunction(newlist):
#     x=set(newlist)
#     return x
# newlist=[3,4,6,3,2,7,4,9,2,6,5,9,400]
# print(dupfunction(newlist))