import bisect

N, T = input().split()
N = int(N)
S = [input() for _ in range(N)]
M = len(T)

pref = []
suf = []

for s in S:
    # prefix
    p = 0
    for c in s:
        if p < M and c == T[p]:
            p += 1
    pref.append(p)

    # suffix
    q = 0
    for c in reversed(s):
        if q < M and c == T[M - 1 - q]:
            q += 1
    suf.append(q)

suf.sort()

ans = 0
for p in pref:
    need = M - p
    idx = bisect.bisect_left(suf, need)
    ans += len(suf) - idx

print(ans)
