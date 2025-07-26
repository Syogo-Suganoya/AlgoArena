A = list(map(int, input().split()))
res = "".join(chr(ord("a") + a - 1) for a in A)
print(res)
