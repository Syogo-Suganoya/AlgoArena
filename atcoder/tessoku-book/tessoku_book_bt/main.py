h, w, K = map(int, input().split())
S = [input() for _ in range(h)]
r = [0] * h
c = [0] * w
for i in range(w):
    t = [s[i] for s in S]
    c[i] = t.count(".")

ans = 0
for i in range(1 << h):
    cnt = i.bit_count()
    if cnt > K:
        continue
    nc = c.copy()
    for j in range(h):
        if i & (1 << j):
            for k in range(w):
                if S[j][k] == ".":
                    nc[k] -= 1
    nc.sort()
    ans = max(ans, h * w - sum(nc[: w - (K - cnt)]))
print(ans)
