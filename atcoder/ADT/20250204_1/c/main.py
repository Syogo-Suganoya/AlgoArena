N = int(input())
w = []
x = []
for _ in range(N):
    wi, xi = map(int, input().split())
    w.append(wi)
    x.append(xi)

res = 0
for t in range(24):
    num = 0
    for i in range(N):
        real_t = (t + x[i]) % 24
        if 9 <= real_t < 18:
            num += w[i]
    res = max(res, num)

print(res)
