H = int(input())

for digit in range(10):
    A = H * 10 + digit
    B = A // 10

    if A - B == H:
        print(A)
        break
else:
    print(-1)
