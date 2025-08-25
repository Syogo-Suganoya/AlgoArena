N, M = map(int, input().split())
res = (N + M) % 12
if res == 0:
    res = 12
print(res)
