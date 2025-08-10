N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

res = 0
for i in range(N):
    v = V[i]
    c = C[i]
    r = v - c
    if r > 0:
        res += r
print(res)
