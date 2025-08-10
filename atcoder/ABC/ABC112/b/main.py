N, M = map(int, input().split())
res = float("inf")
for i in range(N):
    A, B = map(int, input().split())
    if B > M:
        continue
    res = min(res, A)

if res != float("inf"):
    print(res)
else:
    print("TLE")
