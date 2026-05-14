# number=input("Enter a number:") #take user input
# inputvalue=float(number)  #convert float
# print(inputvalue)       #print float value
# integarpart=int(inputvalue)     #integer value
# decimalpart=inputvalue-integarpart      #decimal value
# print(integarpart)
# print(decimalpart)

# number = input("Enter a number: ") # Keep original string to count zeros
# inputvalue = float(number)
# print(inputvalue)
#
# integarpart = int(inputvalue)
# decimalpart = inputvalue - integarpart
#
# # 1. Count how many digits are after the decimal in the user's input
# precision = len(number.split(".")[1]) if "." in number else 0
#
# print(integarpart)
#
# # 2. Use an f-string to force Python to show that specific number of zeros
# print(f"{decimalpart:.{precision}f}")


# number = input("Enter a number:")        # take user input
# inputvalue = float(number)               # convert float
# print(inputvalue)                        # print float value
# integerpart = int(inputvalue)            # integer value
#
# # split the input string by "." and take the right side
# print(type(number))
# decimalpart = number.split(".")[1]
#
# print(integerpart)
# print(len(decimalpart))

# from decimal import Decimal
# number = Decimal("100.0000")       # take user input
# print(type(number))
# integerpart = int(number)
# decimalpart = number - integerpart
#
# print(integerpart)
# print(len(decimalpart))
