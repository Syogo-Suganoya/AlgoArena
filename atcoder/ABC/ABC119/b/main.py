N = int(input())
res = 0
for i in range(N):
    A, B = map(str, input().split())
    A = float(A)
    if B == "BTC":
        A *= 380000
    res += A

print(res)
