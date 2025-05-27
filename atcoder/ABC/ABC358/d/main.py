from sortedcontainers import SortedList

N, M = map(int, input().split())
A = list(map(int, input().split()))
H = list(map(int, input().split()))

A = SortedList(A)

res = 0
for h in H:
    idx = A.bisect_left(h)
    if idx >= len(A):
        print(-1)
        exit()
    res += A.pop(idx)

print(res)
