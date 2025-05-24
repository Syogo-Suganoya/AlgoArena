N = int(input())
res = 0
for _ in range(N):
    u, v = map(int, input().split())
    l = len(str(v))
    t = ((v * 1000) / u) / 1000
    res += t
print(res)
