import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

l = 0
r = 10**9 + 1
while r - l > 1:
    m = (l + r) // 2
    p = bisect.bisect_right(A, m)
    q = bisect.bisect_left(B, m)
    if p >= M - q:
        r = m
    else:
        l = m
print(r)
