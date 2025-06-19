from sortedcontainers import SortedSet

A, B, K = map(int, input().split())
s = SortedSet()

# 前からK個
for i in range(A, min(B + 1, A + K)):
    s.add(i)

# 後ろからK個
for i in range(B, max(A - 1, B - K), -1):
    s.add(i)

print(*s)
