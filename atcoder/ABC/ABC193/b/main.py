N = int(input())

res = float("inf")
for i in range(N):
    A, P, X = map(int, input().split())
    X -= A
    if X <= 0:
        continue
    res = min(res, P)

if res == float("inf"):
    res = -1
print(res)
