from math import ceil

A, B, C, D = map(int, input().split())

AD = ceil(A / D)
CB = ceil(C / B)

if AD >= CB:
    print("Yes")
else:
    print("No")
