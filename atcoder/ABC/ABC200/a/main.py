N = int(input())
res = int(N // 100) + 1
if N % 100 == 0:
    res -= 1
print(res)
