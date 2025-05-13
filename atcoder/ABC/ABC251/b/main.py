from itertools import combinations

N, W = map(int, input().split())
A = list(map(int, input().split()))

c = []
for r in range(1, 3 + 1):
    c.extend(combinations(A, r))

s = set()
for i in c:
    tmp = sum(i)
    if W >= tmp:
        s.add(tmp)
print(len(s))
