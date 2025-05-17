A, B = map(float, input().split())
b = int(str(B).replace(".", "").ljust(3, "0"))
s = int(A) * b // 100
print(s)
