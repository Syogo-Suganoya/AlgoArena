N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

res = P
res = min(res, Q + min(D))
print(res)
