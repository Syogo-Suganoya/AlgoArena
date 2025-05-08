import collections

N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))

res = 0
c = collections.Counter(C)

for k, v in c.items():
    t = P[0]
    if k in D:
        t = P[D.index(k) + 1]
    res += t * v

print(res)
