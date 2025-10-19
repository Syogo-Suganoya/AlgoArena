S, A, B, X = map(int, input().split())

t = 0
res = 0

while t < X:
    nxt = min(X, t + A)
    res += (nxt - t) * S

    t = nxt
    if t != X:
        t += B

print(res)
