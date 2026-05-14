#######    Check if a string contains only digits.
x="123"
i=0
while i<len(x):
    if x[i] not in '123456789':     ######  any index e "1234567890" bade onno kisu thaklei ""Not Digit"" print korbe
        print("Not Digit")
        break
    i+=1
else:
    print("Digit")


# x = "123"
# if x.isdigit():
#     print("Digit")
# else:
#     print("Not All Digits")
