N, M = map(int, input().split())
S = input()

S += "0"
res = 0
n = M
r = 0

for c in S:
    if c == "0":
        res = min(res, min(0, n) + r)
        n = M
        r = 0
    elif c == "1":
        n -= 1
    elif c == "2":
        r -= 1

print(-res)
